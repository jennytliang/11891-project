from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for x, y in zip(a, b):
        if x == y:
            r += "0"
        else:
            r += "1"
    return r


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Inputs are two lists a and b each containing only strings of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list.
    >>> string_xor_list(['010', '101'], ['110', '100'])
    ['100', '001']
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""
    if len(a) != len(b):
        raise Exception("Lists must be the same length")
    return [string_xor(x, y) for x, y in zip(a, b)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
