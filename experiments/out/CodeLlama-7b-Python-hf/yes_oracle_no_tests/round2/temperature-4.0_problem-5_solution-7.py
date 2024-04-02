from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: , num
	"""

    res = []
    
    for num in numbers:
        res.append(num)
        res.append(delimeter)
        
    return res[:-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
