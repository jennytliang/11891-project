from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    return " ".join(str(int(a[i] != b[i])) for i in range(len(a)))


def string_xor_alt(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    return " ".join(str(int(a[i] != b[i])) for i in range(len(a)))


def string_xor_alt2(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    return " ".join(str(int(a[i] != b[i])) for i in range(len(a)))


def sum_digits(n: int) -> int:
    """ Input is a natural number n. Return the sum of the digits in n.
    >>> sum_digits(10)
    1
    >>> sum_digits(12345)
    15
    """
    return sum(int(i) for i in str(n))


def sum_digits_alt(n: int) -> int:
    """ Input is a natural number n. Return the sum of the digits in n.
    >>> sum_digits(10)
    1
    >>> sum_digits(12345)
    15
    """
    return sum(int(