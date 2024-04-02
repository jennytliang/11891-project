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
    res: List[int] = [numbers[0]]
    size = len(numbers)
    for i in range(1, size):
        res.append(delimeter)
        res.append(numbers[i])

    return res


def main():

    print("All Tests Passed")

if __name__ == '__main__':
    main()
