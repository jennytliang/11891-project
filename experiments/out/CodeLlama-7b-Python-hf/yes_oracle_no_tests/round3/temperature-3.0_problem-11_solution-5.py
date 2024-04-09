from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: ret = ""
	"""
    return " ".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of integers.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    """
    return [int(a[i]) ^ int(b[i]) for i in range(len(a))]


def string_xor_int(a: str, b: str) -> int:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as an integer.
    >>> string_xor_int('010', '110')
    100
    """
    return int("".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))]), 2)


def string_xor_bytes(a: str, b: str) -> bytes:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as an integer.
    >>> string_xor_bytes('010', '110')
    b'100'
    """
    return bytes([int(a[i]) ^ int(b[i]) for i in range(len(a))])


def string_xor_bytearray(a: str, b: str) -> bytearray:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as an integer.
    >>> string_xor_bytearray('010', '110')
    bytearray(b'100')
    """
    return bytearray([int(a[i]) ^