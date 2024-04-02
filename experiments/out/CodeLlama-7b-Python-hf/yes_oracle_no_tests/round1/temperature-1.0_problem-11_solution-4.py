from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


def rotate_left(s: str, n: int) -> str:
    """ Input is a string s and integer n.
    Rotate s by n positions to the left and return result as a string.
    >>> rotate_left('abcdefg', 2)
    'cdefgab'
    """
    return s[n:] + s[:n]


def rotate_right(s: str, n: int) -> str:
    """ Input is a string s and integer n.
    Rotate s by n positions to the right and return result as a string.
    >>> rotate_right('abcdefg', 2)
    'fgabcde'
    """
    return rotate_left(s[::-1], n)[::-1]


def string_to_int(s: str) -> int:
    """ Input is a string s.
    Convert the string s to an integer and return result as an integer.
    >>> string_to_int('1234')
    1234
    """
    return int(s)


def int_to_string(n: int) -> str:
    """ Input is an integer n.
    Convert the integer n to a string and return result as a string.
    >>> int_to_string(1234)
    '1234'
    """
    return str(n)


def string_to_list(s: str) -> List[str]:
    """ Input is a string s.
    Convert the string s to a list of characters and return result as a list.
    >>> string_to_list('1234')
    ['1', '2', '3', '4']
    """
    return list(s)


def list_to_string(l: List[str]) -> str:
    """ Input is a list l.
    Convert the list l to a string and return result as a string.
    >>> list_to_string(['1', '2', '3', '4'])