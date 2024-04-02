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
            r += "0"
        else:
            r += "1"
    return r


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input is two lists of strings a and b.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['111', '111'])
    ['001', '100']
    """

    r = []
    for i in range(len(a)):
        r.append(string_xor(a[i], b[i]))
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
