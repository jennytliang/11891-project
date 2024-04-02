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
  
        if i == 0:
            res.append(numbers[i])
        elif i == len(numbers) - 1:
            res.append(numbers[i])
        else:
            res.append(numbers[i])
            res.append(delimeter)

    return res


if __name__ == "__main__":
    print(intersperse([1, 2, 3], 4))
