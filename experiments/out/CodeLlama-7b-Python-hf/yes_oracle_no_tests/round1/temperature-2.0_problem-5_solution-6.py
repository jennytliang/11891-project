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
    # BEGIN_SOLUTION
    res = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            res.append(numbers[i])
        else:
            res.append(delimeter)
            res.append(numbers[i])
    return res
    # END_SOLUTION
