from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res
	Do not include these tokens in the code: result
	"""
    res = []
    for i in range(len(numbers)):
        res.append(numbers[i])
        if i < len(numbers)-1:
            res.append(delimeter)
    return res


def flatten(list_of_lists: List[List[int]]) -> List[int]:
    """ Flatten a list of lists into a single list
    >>> flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
	Include these tokens in the code: result
	Do not include these tokens in the code: res
	"""
    result = []
    for i in range(len(list_of_lists)):
        result.extend(list_of_lists[i])
    return result


def is_sublist(lst1: List[int], lst2: List[int]) -> bool:
    """ Returns True if lst1 is a sublist of lst2
    >>> is_sublist([1, 2, 3], [1, 2, 3, 1, 2, 3])
    True
    >>> is_sublist([1, 2, 3], [1, 2, 3, 4, 5])
    True
    >>> is_sublist([1, 2, 3], [1, 2, 4, 5])
    False
    
	Include these tokens in the code: i, j, lst2_len
	Do not include these tokens in the code: lst2_len
	"""
    i = 0
    j = 0
    lst1_len =