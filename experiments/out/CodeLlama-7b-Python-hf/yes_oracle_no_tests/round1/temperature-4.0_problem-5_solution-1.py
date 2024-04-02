from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res = []
	"""
    res = []
    for i in range(len(numbers) - 1):
        res.append(numbers[i])
        res.append(delimeter)
    res.append(numbers[-1])
    return res


def intersperse_rec(numbers: List[int], delimeter: int) -> List[int]:
    """Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_rec([], 4)
    []
    >>> intersperse_rec([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res = []
	"""
    if not numbers:
        return []
    elif len(numbers) == 1:
        return numbers
    else:
        return [numbers[0]] + [delimeter] + intersperse_rec(numbers[1:], delimeter)
