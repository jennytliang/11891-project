from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ''
    for i, j in zip(a, b):
        if i == j:
            r += '0'
        else:
            r += '1'

    return r


def string_xor_lists(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_lists(['010', '110'], ['110', '010'])
    ['100', '100']
    """

    r = []
    for i, j in zip(a, b):
        r.append(string_xor(i, j))

    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
