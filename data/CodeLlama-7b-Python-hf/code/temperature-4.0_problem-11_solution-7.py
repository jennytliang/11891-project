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
    #return ''.join([str(i/100000 - round(i//10000 - i//4000*10)) for i in int2flt(list('00{}'.format(float(s))))[0]]) 
    """ Input are two strings(numbers) in a, b.
        If these numbers are represented in base 2 with the string 101 being the integer representation of 5 (base-2), the function should xor these numbers, which is represented by x1.
        Finally, the xor string is returned as integer.
        >>> string2int('111')
        7.0
    """

############################################1233#########2223
def string_xor(a:'int_list_convertible_string', b):  
    """Input are int_lists
        If these numbers are represented in base <any int base>,
        with the a's nth element being th nth digit/character, representing integer value of that digit as if in math.
        Then the result is a - b
        If all these strings are xor_list of integers, then do not convert to xor list, and return result of xoring two int lists:
        print(xor_str(a,'49300')) # a = [493, 54445, 544054445]     xor_string of a with string '49300' = 99200, which is xor(493^63^1999) = 200.  
    """   
    try:
        a, b = int_list(str(a), 10), [int(i,2) for i in list(list2biti(b))] # a, b =  list, list
        
        return reduce(lambda x, y: x^(y), a) ^ reduce(lambda x,y : x^y, b)  # return xor of list_a and list b: 