from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ret += "0"
        else:
            ret += "1"

    return ret


def string_not(a: str) -> str:
    """ Input is a string a consisting only of 1s and 0s.
    Perform binary NOT on this input and return result also as a string.
    >>> string_not('010')
    '101'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for i in range(len(a)):
        if a[i] == "0":
            ret += "1"
        else:
            ret += "0"

    return ret


def get_index(a: List[int], value: int) -> int:
    """ Input is a list of integers a and an integer value.
    Return the index of the first occurrence of value in a,
    or return -1 if value is not in a.
    >>> get_index([2, 4, 6, 8], 6)
    2
    
	Include these tokens in the code: ".
	"""

    for i in range(len(a)):
        if a[i] == value:
            return i

    return -1


def get_all_indexes(a: List[int], value: int) -> List[int]:
    """ Input is a list of integers a and an integer value.
    Return all the indexes of the first occurrence of value in a,
    or return an empty list if value is not in a.
    >>> get_all_indexes([2, 4, 6, 8, 4, 6, 2], 6)
    [2, 4]
    
	Include these tokens in the code: ".
	"""

    ret = []
    for i in range(len(a)):
        if a[i] == value:
            ret.append(i)

    return ret


def get_smallest_int(a: List[