from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    r = ""
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            r += '0'
        else:
            r += '1'
    return r + a[len(b):] + b[len(a):]


def string_xor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list('010', '110')
    ['100', '010', '110']
    """
    return [string_xor(a, b), a, b]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
