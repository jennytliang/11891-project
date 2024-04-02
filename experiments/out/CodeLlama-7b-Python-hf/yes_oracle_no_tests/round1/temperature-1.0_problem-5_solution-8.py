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
    
    for index, number in enumerate(numbers):
        res.append(number)
        if index != len(numbers) - 1:
            res.append(delimeter)

    return res


if __name__ == "__main__":
    print(intersperse([], 4))
    print(intersperse([1, 2, 3], 4))
