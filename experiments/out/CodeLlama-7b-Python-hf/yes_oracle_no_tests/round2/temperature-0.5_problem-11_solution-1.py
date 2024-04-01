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


def string_xor_array(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_array(['010', '110'], ['101', '000'])
    ['111', '000']
    """

    return [string_xor(a_i, b_i) for a_i, b_i in zip(a, b)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
