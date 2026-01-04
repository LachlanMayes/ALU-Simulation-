
# 4-Bit ALU Simulator

A Python-based simulation of a **4-bit Arithmetic Logic Unit (ALU)**. This project demonstrates how digital logic circuits work by implementing low-level logic gates (AND, OR, XOR) and full adders using software bitwise operators, rather than relying on high-level arithmetic operators.

## 📖 Overview

In computer architecture, the ALU is the heart of the CPU, responsible for performing arithmetic and logic operations. This project simulates that hardware behavior in Python.

Unlike standard Python programming where `a + b` is calculated instantly, this project constructs the result bit-by-bit using a simulated **Ripple Carry Adder**. It handles:
*   4-bit integer inputs (0-15 unsigned, -8 to 7 signed).
*   Status Flags (Carry, Zero, Negative).
*   2's Complement logic for subtraction.

## ✨ Features

*   **Low-Level Simulation:** Implements `Half Adder` and `Full Adder` logic.
*   **4-Bit Architecture:** Results are masked to 4 bits (`0xF`).
*   **5 Supported Operations:** ADD, SUBTRACT, AND, OR, XOR.
*   **Status Flags:**
    *   **C (Carry):** Indicates an overflow out of the MSB (Most Significant Bit).
    *   **Z (Zero):** Set if the result is 0.
    *   **N (Negative):** Set if the MSB is 1 (indicating a negative number in 2's complement).

## 🛠️ Technical Details

The ALU accepts an **Opcode** (Control Signal) to determine which operation to perform. The simulation is structurally designed as follows:

1.  **Logic Gates:** Uses Python bitwise operators (`&`, `|`, `^`, `~`) to simulate hardware gates.
2.  **Adders:**
    *   `half_adder(a, b)`: Computes sum and carry.
    *   `full_adder(a, b, carry_in)`: Computes sum and carry considering an input carry.
    *   `four_bit_adder(a, b)`: Chains four full adders together.
3.  **ALU Multiplexing:** Calculates results for all operations in parallel (simulating hardware signal propagation) and selects the specific result based on the Opcode.

## 🚀 Usage

### Opcodes
The ALU uses a bit-mask style opcode system (One-Hot encoding logic):

| Operation | Opcode (Integer) | Opcode (Binary) |
| :--- | :---: | :---: |
| **ADD** | `1` | `00001` |
| **SUB** | `2` | `00010` |
| **AND** | `4` | `00100` |
| **OR** | `8` | `01000` |
| **XOR** | `16` | `10000` |

### Example Code

```python
from alu_code import alu

# Define Opcodes
OP_ADD = 1
OP_SUB = 2

# Example 1: Addition (5 + 3)
# 0101 + 0011 = 1000 (8)
result, carry, zero, neg = alu(5, 3, OP_ADD)
print(f"Result: {result}, Carry: {carry}") 
# Output: Result: 8, Carry: 0

# Example 2: Subtraction (5 - 3)
# Uses 2's complement logic internally
result, carry, zero, neg = alu(5, 3, OP_SUB)
print(f"Result: {result}, Negative Flag: {neg}")
# Output: Result: 2, Negative Flag: 0

# Example 3: Overflow (15 + 1)
# 1111 + 0001 = 0000 (with carry)
result, carry, zero, neg = alu(15, 1, OP_ADD)
print(f"Result: {result}, Carry: {carry}, Zero Flag: {zero}")
# Output: Result: 0, Carry: 1, Zero Flag: 1
```

## 🧪 Testing

The project includes a test suite using `pytest` to verify logic gates, arithmetic correctness, and flag states.

### Prerequisites
You need `pytest` installed:
```bash
pip install pytest
```

### Running Tests
Run the tests using the command line:
```bash
pytest test_alu.py
```

The tests cover:
*   Addition (Standard and Overflow/Carry checks).
*   Subtraction (Positive and Negative results).
*   Logic Operations (AND, OR, XOR truth tables).
*   Flag verification (Zero, Carry, Negative).

## 📂 File Structure

*   `alu_code.py`: Contains the `half_adder`, `full_adder`, `four_bit_adder`, and main `alu` function.
*   `test_alu.py`: Contains unit tests using `pytest`.

## ⚠️ Limitations

*   This is a **4-bit** simulator. Passing integers larger than 15 (e.g., `alu(20, 5, 1)`) will only process the lowest 4 bits of the input.
*   The subtraction logic assumes 2's complement representation.
