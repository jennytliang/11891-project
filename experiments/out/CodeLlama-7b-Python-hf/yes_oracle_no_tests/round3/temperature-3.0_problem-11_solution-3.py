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


def rotate_left(a: List[int], k: int) -> List[int]:
    """ Input is a list of numbers a and a number k.
    Rotate all numbers in a by k positions to the left.
    >>> rotate_left([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = a[k:] + a[:k]
    return r


def rotate_right(a: List[int], k: int) -> List[int]:
    """ Input is a list of numbers a and a number k.
    Rotate all numbers in a by k positions to the right.
    >>> rotate_right([1, 2, 3, 4, 5], 2)
    [3, 4, 5, 1, 2]
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = a[-k:] + a[:-k]
    return r


def string_xor_list(a: str, b: List[int]) -> List[int]:
    """ Input is a string a and a list of numbers b.
    Perform binary XOR on the string a and all numbers in b.
    Return the result as a list of numbers.
    >>> string_xor_list('010', [1, 2, 3])
    [1, 1, 3]
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = []
    for i in range(len(b)):
        if a[i] == b[i]:
            r.append(0