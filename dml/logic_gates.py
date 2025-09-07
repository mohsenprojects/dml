def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a, bit_length=32):
    mask = (1 << bit_length) - 1
    return (~a) & mask

def NAND(a, b, bit_length=32):
    return NOT(AND(a, b), bit_length)

def NOR(a, b, bit_length=32):
    return NOT(OR(a, b), bit_length)

def XOR(a, b):
    return a ^ b

def XNOR(a, b, bit_length=32):
    return NOT(XOR(a, b), bit_length)

def SHL(a, n_bits=1):
    return a << n_bits

def SHR(a, n_bits=1):
    return a >> n_bits

def arithmetic_shift_right(a, n_bits=1, bit_length=32):
    if a & (1 << (bit_length - 1)):
        mask = (1 << bit_length) - 1
        return (a >> n_bits) | (~(mask >> n_bits) & mask)
    return a >> n_bits

def rotate_left(a, n_bits, bit_length=32):
    n_bits = n_bits % bit_length
    mask = (1 << bit_length) - 1
    return ((a << n_bits) | (a >> (bit_length - n_bits))) & mask

def rotate_right(a, n_bits, bit_length=32):
    n_bits = n_bits % bit_length
    mask = (1 << bit_length) - 1
    return ((a >> n_bits) | (a << (bit_length - n_bits))) & mask

#-----------------------------------------------------------------------

def multi_input_AND(*numbers, bit_length=32):
    result = (1 << bit_length) - 1
    for num in numbers:
        result &= num
    return result

def multi_input_OR(*numbers, bit_length=32):
    result = 0
    for num in numbers:
        result |= num
    return result & ((1 << bit_length) - 1)

def multi_input_XOR(*numbers, bit_length=32):
    result = 0
    for num in numbers:
        result ^= num
    return result & ((1 << bit_length) - 1)