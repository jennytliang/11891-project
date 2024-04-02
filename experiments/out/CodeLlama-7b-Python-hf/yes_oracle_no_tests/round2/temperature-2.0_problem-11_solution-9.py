from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	"""
    return " ".join(str(int(a, 2) ^ int(b, 2))) for a, b in zip(a, b))


def string_xor_list(a: str, b: List[str]) -> List[str]:
    """ Input is a string and a list of strings.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list('010', ['110', '100'])
    ['100', '010']
    """
    return [string_xor(a, b) for b in b]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
