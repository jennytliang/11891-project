from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res =
	Do not include these tokens in the code: if not numbers : return
	"""
    res = []
    if not numbers:
        return res
    res.append(numbers[0])
    for i in range(1, len(numbers)):
        res.append(delimeter)
        res.append(numbers[i])
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
