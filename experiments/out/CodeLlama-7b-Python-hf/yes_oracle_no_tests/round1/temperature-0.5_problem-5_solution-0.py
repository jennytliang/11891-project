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

    r = []
    for i in range(len(numbers)):
        r.append(numbers[i])
        if i != len(numbers) - 1:
            r.append(delimeter)

    res = r
    return res


def intersperse_rec(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_rec([], 4)
    []
    >>> intersperse_rec([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: numbers, delimeter, res, result
	Do not include these tokens in the code:
    """
    if numbers == []:
        res = []
    else:
        res = [numbers[0]]
        res += [delimeter]
        res += intersperse_rec(numbers[1:], delimeter)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
