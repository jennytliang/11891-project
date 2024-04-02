from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_2(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_2('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str
	Do not include these tokens in the code: x or _ list = []
	"""
    return " ".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_3(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_3('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str
	Do not include these tokens in the code: x or _ list = []
	"""
    return " ".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_4(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_4('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str
	Do not include these tokens in the code: x or _ list = []
	"""
    return " ".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string