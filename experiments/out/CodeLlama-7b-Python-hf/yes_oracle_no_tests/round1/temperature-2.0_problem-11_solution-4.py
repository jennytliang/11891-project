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
    for i in range(len(a)):
        r += str(int(a[i]) ^ int(b[i]))
    return r


def string_xor_all(xor_list: List[str]) -> str:
    """ Input is a list of strings.
    Perform binary XOR on all the strings in the list and return result also as a string.
    >>> string_xor_all(['010', '110'])
    '100'
    """

    r = xor_list[0]
    for i in range(len(xor_list)):
        if i == 0:
            continue
        r = string_xor(r, xor_list[i])
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
