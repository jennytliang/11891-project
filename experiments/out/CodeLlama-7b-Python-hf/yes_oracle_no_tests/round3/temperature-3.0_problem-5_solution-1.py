from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res . append ( numbers [ i ])
	"""


    res = []
    
    for i in range(len(numbers) - 1):
        res.append(numbers[i])
        res.append(delimeter)
    res.append(numbers[-1])

    return res



def intersperse_rec(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse_rec([], 4)
    []
    >>> intersperse_rec([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res . append ( numbers [ i ])
	"""


    res = []

    if len(numbers) == 0:
        return res

    res.append(numbers[0])

    return intersperse_rec(numbers[1:], delimeter) + [delimeter] + res




if __name__ == '__main__':
    import doctest
    doctest.testmod()
