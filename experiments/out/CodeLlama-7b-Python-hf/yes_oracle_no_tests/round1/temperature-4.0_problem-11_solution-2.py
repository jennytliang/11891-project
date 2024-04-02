from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: " ". join ( str
	"""

    r = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            r += "1"
        else:
            r += "0"
    return r


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as list of integers.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: " ". join ( list
	"""

    r = []
    for i in range(len(a)):
        if a[i] != b[i]:
            r.append(1)
        else:
            r.append(0)
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
