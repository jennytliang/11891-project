from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: ".
	"""

    ret_str = ""
    for a_char, b_char in zip(a, b):
        if a_char == b_char:
            ret_str += "0"
        else:
            ret_str += "1"

    return ret_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()
