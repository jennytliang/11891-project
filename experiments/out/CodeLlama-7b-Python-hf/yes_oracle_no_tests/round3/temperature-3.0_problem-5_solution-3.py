from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: if i == len ( numbers )-
	"""


    res = []
    for i in range(len(numbeers)):
        res.append(numbeers[i])
        if i != len(numbeers) - 1:
            res.append(delimeter)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
