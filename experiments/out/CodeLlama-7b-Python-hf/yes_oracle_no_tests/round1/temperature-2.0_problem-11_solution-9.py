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
    for i, j in zip(a, b):
        if i == j:
            r += "0"
        else:
            r += "1"
    return r


def string_xor_with_lists(a: List[int], b: List[int]) -> List[int]:
    """ Input are two lists a and b consisting of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list.
    >>> string_xor_with_lists([0, 1, 0], [1, 1, 0])
    [1, 0, 0]
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = []
    for i, j in zip(a, b):
        if i == j:
            r.append(0)
        else:
            r.append(1)
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
