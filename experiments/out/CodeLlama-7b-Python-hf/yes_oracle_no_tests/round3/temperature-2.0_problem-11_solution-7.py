from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: str ( int
	Do not include these tokens in the code: [" 0 " if a _ i == b _
	"""

    return "".join(["0" if a[i] == b[i] else "1" for i in range(len(a))])


def string_xor_noncompliant(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: str ( int
	Do not include these tokens in the code: [" 0 " if a _ i == b _
	"""

    if len(a) != len(b):
        raise ValueError("a and b must be the same length")

    return "".join(["0" if a[i] == b[i] else "1" for i in range(len(a))])


if __name__ == "__main__":
    import doctest

    doctest.testmod()