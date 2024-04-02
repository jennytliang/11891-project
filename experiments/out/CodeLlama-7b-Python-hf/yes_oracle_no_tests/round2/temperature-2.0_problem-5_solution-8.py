from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: if not numbers : return res
	"""

    res = []
    for i in range(len(numbers)):
        res.append(numbers[i])
        if i + 1 < len(numbers):
            res.append(delimeter)
    return res


if __name__ == "__main__":
    print(intersperse([], 4))
    print(intersperse([1, 2, 3], 4))
