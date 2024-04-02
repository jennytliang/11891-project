from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	"""
    return " ".join(str(int(a, 2) ^ int(b, 2))) for a, b in zip(a.split(), b.split()))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list(['010', '110'], ['001', '011'])
    ['100', '100']
    """
    return [string_xor(a, b) for a, b in zip(a, b)]


def string_xor_list_of_lists(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of lists a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of lists.
    >>> string_xor_list_of_lists([['010', '110'], ['001', '011']], [['001', '011'], ['100', '100']])
    [['100', '001'], ['100', '100']]
    """
    return [string_xor_list(a, b) for a, b in zip(a, b)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
