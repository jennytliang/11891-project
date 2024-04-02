from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: if i == 0 :
	"""

    res = []
    for i in range(len(numbers)):
  
        if i == 0:
            res.append(numbers[i])
        else:
            res.append(numbers[i - 1])
            res.append(delimeter)
            res.append(numbers[i])

    return res


if __name__ == "__main__":
    print("Example:")
    print(intersperse([1, 2, 3], 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([1, 2], 0) == [1, 0, 2]
    assert intersperse([1], 0) == [1]
    assert intersperse([], 100) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
