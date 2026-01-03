# Inputs  A = 0000 B = 0000 control signal (Opcode) 
# Outputs 4 bit Result and  set of Flags (status bits)
# operations: ADD = 000, SUBTRACT = 001, AND (Bitwise)= 010, OR (Bitwise) = 100 , XOR (Bitwise) = 011, NOT (Bitwise) = 111

def half_adder(a,b):
    sum =  a ^ b #example: 1 xor 0 if a = 1 and b  = 1 sum =  0 but if a = 0  and b  = 1 result = 1
    carry_out = a & b  #example: a = 1 and b = 0  carry =  0 but a =  1 and b = 1  carry =  1 used to carry over bits in adding
    return sum,carry_out

def full_adder(a,b,carry_in):
    sum =  a ^ b ^ carry_in #example: xor a,b and carry in easier way to picture it (a xor b) xor c so if (a=1 xor b= 1) = 0 xor c =1 sum=1
    carry_out = (a & b) | (a ^ b) & carry_in  #example: do a normal and on a and b or a xor b then check if there is a carry in 
    return sum,carry_out

def four_bit_adder(a,b,carry_in = 0 ):
    sum_0 = sum_1 = sum_2 = sum_3 = 0 #sum 0 to 3 represent our 4 bits
    current_carry = carry_in #our current carry over 
    final_sum = 0 #final sum of the adder which will be binary but then to interger bc of python default
    '''start of sequentially get zero bit of a num and b num  and 1 to check if it's 1 or 0 then use them as the parameters in the 
     full adder function we assign the result of the sum of the 0th bit to sum0 and if there is a carry over bit to current carry 
    and just repeat the steps until we have all 4 sum bits '''
    bit_a = (a >> 0) & 1
    bit_b = (b >> 0) & 1
    sum_0,current_carry = full_adder(bit_a,bit_b,current_carry)
    final_sum = final_sum | (sum_0 << 0)
    bit_a = (a >> 1) & 1
    bit_b = (b >> 1) & 1
    sum_1,current_carry = full_adder(bit_a,bit_b,current_carry)
    final_sum = final_sum | (sum_1 << 1)
    bit_a = (a >> 2) & 1
    bit_b = (b >> 2) & 1
    sum_2,current_carry = full_adder(bit_a,bit_b,current_carry)
    final_sum = final_sum | (sum_2 << 2)
    bit_a = (a >> 3) & 1
    bit_b = (b >> 3) & 1
    sum_3,current_carry = full_adder(bit_a,bit_b,current_carry)
    final_sum = final_sum | (sum_3 << 3)
    return final_sum,current_carry

def alu(a,b, opcode):
    #initialising the opcodes and checking bit postion 
    op0 = opcode & 1
    op1 = (opcode >> 1) & 1 
    op2 = (opcode >> 2) & 1
    op3 = (opcode >> 3) & 1
    op4 = (opcode >> 4) & 1

# assigning the opcodes to the function
    is_add = (op0 & 1) & (~op1 & 1) & (~op2 & 1) & (~op3 & 1) & (~op4 & 1)
    is_sub = (op1 & 1) & (~op0 & 1) & (~op2 & 1) & (~op3 & 1) & (~op4 & 1)
    is_and = (op2 & 1) & (~op0 & 1) & (~op1 & 1) & (~op3 & 1) & (~op4 & 1)
    is_or =(op3 & 1) & (~op0 & 1) & (~op1 & 1) & (~op2 & 1) & (~op4 & 1)
    is_xor = (op4 & 1) & (~op0 & 1) & (~op1 & 1) & (~op2 & 1) & (~op3 & 1)
#gathering the results from funtion performed
    add_result, carry_add = four_bit_adder(a,b)
    sub_result, carry_sub = four_bit_adder(a,~b, carry_in = 1)
    and_result = a & b
    or_result =  a | b
    xor_result = a ^ b
    
    carry_result =  ((carry_add & -is_add) | (carry_sub & -is_sub)) #assigning the carry result to be for subtraction or addition 
    result = ((add_result & -is_add) |  (sub_result & -is_sub) | (and_result & -is_and)
               |(or_result & -is_or) | (xor_result & -is_xor)) #assigning the result for one of the 5 actions/funtions 
    is_zero = ~(result | (result>>1) | (result>>2) | (result>>3)) & 1 #check for 0
    is_negative = (result >> 3) & 1 #checks bit 4 (MSB) to see if it's a positive number or negative number
    result = result & 0xF # make sure to only  return 4 bits 
    return result, carry_result, is_zero, is_negative

