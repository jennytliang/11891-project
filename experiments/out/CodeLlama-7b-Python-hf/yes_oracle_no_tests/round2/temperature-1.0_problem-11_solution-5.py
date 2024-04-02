from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: a [
	"""


    return "".join(stinga[i] for i in range(len(a)) if a[i] == b[i])

if __name__ == "__main__":
    import doctest
    doctest.testmod()