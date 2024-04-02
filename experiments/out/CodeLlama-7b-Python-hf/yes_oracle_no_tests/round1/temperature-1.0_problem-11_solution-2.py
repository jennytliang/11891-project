from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(i) ^ int(j)) for i, j in zip(a, b))


def string_xor_all(strings: List[str]) -> str:
    """ Input is a list of strings consisting only of 1s and 0s.
    Perform binary XOR on all the strings and return result also as a string.
    >>> string_xor_all(['010', '110'])
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""
    return "".join(str(int(i) ^ int(j)) for i, j in zip(*strings))


def string_xor_all_list(strings: List[str]) -> List[str]:
    """ Input is a list of strings consisting only of 1s and 0s.
    Perform binary XOR on all the strings and return result as a list of strings.
    >>> string_xor_all_list(['010', '110'])
    ['100', '010']
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""
    return [
        "".join(str(int(i) ^ int(j)) for i, j in zip(*strings)) for strings in zip(*strings)
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
