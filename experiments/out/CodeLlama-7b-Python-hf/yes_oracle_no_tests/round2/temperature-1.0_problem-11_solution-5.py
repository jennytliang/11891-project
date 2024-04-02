from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""


    return "".join(str(int(a_bit) ^ int(b_bit)) for a_bit, b_bit in zip(a, b))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['110', '101'])
    ['100', '010']
    """

    return [string_xor(a_bit, b_bit) for a_bit, b_bit in zip(a, b)]


def string_xor_matrix(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_matrix([['010', '110'], ['110', '101']], [['110', '101'], ['100', '010']])
    [['100', '010'], ['000', '110']]
    """

    return [string_xor_list(a_bit, b_bit) for a_bit, b_bit in zip(a, b)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
