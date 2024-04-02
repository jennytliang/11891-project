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

    for i in range(len(numbers)):
 
        res.append(numbers[i])
 
        if i != len(numbers) - 1:
            res.append(delimeter)
 
    return res


if __name__ == "__main__":
    print(intersperse([1, 2, 3], 4))
