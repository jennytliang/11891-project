from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for i, j in zip(a, b):
        if i == j:
            ret += "0"
        else:
            ret += "1"
    return ret


if __name__ == "__main__":
    import doctest

    doctest.testmod()
