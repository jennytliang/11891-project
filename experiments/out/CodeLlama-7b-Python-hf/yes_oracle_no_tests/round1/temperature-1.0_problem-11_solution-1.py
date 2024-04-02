from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(aa) ^ int(bb)) for aa, bb in zip(a, b))


def string_shift_left(s: str, shift: int) -> str:
    """ Input is a string s and an integer shift.
    Perform left shift on the string s with shift positions and return result.
    >>> string_shift_left('1110111', 2)
    '1111100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""
    if shift == 0:
        return s
    return s[-shift:] + s[:-shift] if s[0] == '0' else s[:-shift-1] + s[-shift:]


def string_shift_right(s: str, shift: int) -> str:
    """ Input is a string s and an integer shift.
    Perform right shift on the string s with shift positions and return result.
    >>> string_shift_right('11', 2)
    '0011'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""
    return s[: shift % len(s)] + s[shift % len(s):]


def binary_to_integer(s: str) -> int:
    """ Input is a binary string representing a positive integer.
    The string represents the unsigned integer. Return the integer value.
    >>> binary_to_integer('11')
    3
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""
    return int(s, 2) if s else 0


def string_inverse_bits(s: str) -> str:
    """ Input is a string s containing 1s and 0s representing 8-bit binary codes.
    Perform inverting bits on s and return result.
    >>> s = '10100010111011'
    string_inverse_bits(s)
    '010111010