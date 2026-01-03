import pytest
from alu_code import alu


OP_ADD = 1
OP_SUB = 2
OP_AND = 4
OP_OR  = 8
OP_XOR = 16

@pytest.mark.parametrize("a, b, expected_res, expected_carry", [
    (0,    0,   0,      0),    # 0 + 0 = 0
    (5,    3,   8,      0),    # 5 + 3 = 8
    (10,   5,   15,     0),    # 10 + 5 = 15 (Max value)
    (15,   1,   0,      1),    # 15 + 1 = 0 (Overflow, Carry 1)
    (15,  15,   14,     1),    # 15 + 15 = 30 (11110 -> res 14, Carry 1)
])
def test_alu_addition(a, b, expected_res, expected_carry):
    res, carry, zero, neg = alu(a, b, OP_ADD)
    
    # Check the values
    assert res == expected_res
    assert carry == expected_carry
    
    # Check flags logic dynamically
    expected_zero = 1 if expected_res == 0 else 0
    assert zero == expected_zero



@pytest.mark.parametrize("a, b, expected_res, expected_neg", [

    (5,    3,  2,     0),   # 5 - 3 = 2 (Positive)
    (10,  10,  0,     0),   # 10 - 10 = 0
    (3,    5,  14,    1),   # 3 - 5 = -2. In 4-bit 2's comp, -2 is 1110 (14). NegFlag=1
    (0,    1,  15,    1),   # 0 - 1 = -1. In 4-bit 2's comp, -1 is 1111 (15). NegFlag=1
])
def test_alu_subtraction(a, b, expected_res, expected_neg):
    res, carry, zero, neg = alu(a, b, OP_SUB)
    
    assert res == expected_res
    assert neg == expected_neg
    
    # Check Zero Flag
    expected_zero = 1 if expected_res == 0 else 0
    assert zero == expected_zero



@pytest.mark.parametrize("a, b, opcode, expected_res", [

    (12, 10, OP_AND, 8),   # 1100 & 1010 = 1000 (8)
    (15,  0, OP_AND, 0),   # 1111 & 0000 = 0000
    
    (5,  10, OP_OR,  15),  # 0101 | 1010 = 1111 (15)
    (0,   0, OP_OR,   0),  # 0 | 0 = 0
    
    (15, 15, OP_XOR,  0),  # 1111 ^ 1111 = 0000
    (10,  5, OP_XOR, 15),  # 1010 ^ 0101 = 1111
])
def test_alu_logic(a, b, opcode, expected_res):
    res, carry, zero, neg = alu(a, b, opcode)
    
    assert res == expected_res
    