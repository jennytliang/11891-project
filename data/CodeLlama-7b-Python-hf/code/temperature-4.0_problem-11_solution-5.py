from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return str(int(a, 2) ^ int(b, 2))

#############################################33333####################################################
def binary_rep(int_number: int, number_of_terms: int = 8):   # by default string is 8 terms/digits long   #
    return "{0:0{width}b}".format(int_number, width=number_of_terms)

#############################################233333333######################
def string_xor2(a:str, b:str, num_terms:int):   # 
    # check a and b is in 01-string format, 
    # check num_char as an integer >= size of a and b (should raise error otherwise) 
    return ''.join([str(bool(float(i)==float(i+j))) for i, j in zip(int2flt_ljust(a,num_terms), int2flt_ljust(b,num_terms))])