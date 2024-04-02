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
    res: List[int] = []
    for i in range(len(numbers) - 1):
        res.append(numbers[i])
        res.append(delimeter)
    res.append(numbers[-1])
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    input_list = [6, 5, 9, 8, 5, 6]
    assert intersperse(input_list, 9) == [6, 9, 5, 9, 9, 8, 9, 5, 9, 6]
    print("All OK")
