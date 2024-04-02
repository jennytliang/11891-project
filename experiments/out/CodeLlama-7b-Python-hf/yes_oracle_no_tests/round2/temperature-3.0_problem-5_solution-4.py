from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: []
	Do not include these tokens in the code: numbers [: 1 ]
	"""

    
    return [n for (i, n) in enumerate(numbers) if i % 2 != 0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
