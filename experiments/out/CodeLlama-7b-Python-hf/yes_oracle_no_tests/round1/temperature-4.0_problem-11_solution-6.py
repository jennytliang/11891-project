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
        if a[i] == b[i]:
            r += '0'
        else:
            r += '1'
    return r


def string_xor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list('010', '110')
    ['0', '1', '0']
    """
    return [a[i] if a[i] == b[i] else '1' for i in range(len(a))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
