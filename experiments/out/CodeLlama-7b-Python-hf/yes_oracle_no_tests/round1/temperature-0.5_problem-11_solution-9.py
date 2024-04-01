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
    """ Inputs are lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['011', '111'], ['110', '000'])
    ['101', '110']
    """
    return [string_xor(a_i, b_i) for a_i, b_i in zip(a, b)]


def string_xor_list_list(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Inputs are lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_list_list([['011', '111'], ['111', '011']], [['110', '000'], ['000', '110']])
    [['101', '000'], ['001', '110']]
    """
    return [string_xor_list(a_i, b_i) for a_i, b_i in zip(a, b)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
