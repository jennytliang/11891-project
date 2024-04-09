from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	"""
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    return " ".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_by_list(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	"""
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    list_a = a.split(" ")
    list_b = b.split(" ")
    return " ".join(str(int(list_a[i]) ^ int(list_b[i])) for i in range(len(list_a)))


def string_xor_by_list_comprehension(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	"""
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    list_a = a.split(" ")
    list_b = b.split(" ")
    return " ".join([str(int(list_a[i]) ^ int(list_b[i])) for i in range(len(list_a))])


def string_xor_by_list_comprehension_and_split(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and