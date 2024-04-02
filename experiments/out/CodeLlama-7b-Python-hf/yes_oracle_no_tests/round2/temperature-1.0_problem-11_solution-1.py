from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: a [ i ])
	Do not include these tokens in the code: aa )
	"""


    return "".join(st[i] for st in zip(a, b) for i in range(len(st)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
