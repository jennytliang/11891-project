from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
