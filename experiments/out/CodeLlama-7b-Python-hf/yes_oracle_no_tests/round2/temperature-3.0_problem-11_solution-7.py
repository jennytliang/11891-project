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
    for i in range(len(a)):
        if a[i] == b[i]:
            r += "0"
        else:
            r += "1"
    return r


def list_xor(a: List[int], b: List[int]) -> List[int]:
    """ Input are two lists a and b consisting of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list.
    >>> list_xor([1, 0, 1, 0, 1], [1, 1, 1, 0, 0])
    [0, 1, 0, 1, 1]
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append(0)
        else:
            r.append(1)
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
