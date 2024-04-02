from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""


    return "".join(str(int(i) & int(j)) for i, j in zip(a, b))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
