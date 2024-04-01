from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""


    return "".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input is two lists of strings each containing only 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list(['110'], ['011'])
    ['101']
    """

    return ["".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a_string, b_string)) for a_string, b_string in zip(a, b)]


def string_xor_list_list(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input is two lists of lists of strings each containing only 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of lists of strings.
    >>> string_xor_list_list([['010']], [['110']])
    [['100']]
    """

    return [["".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a_string, b_string)) for a_string, b_string in zip(a_list, b_list)] for a_list, b_list in zip(a, b)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
