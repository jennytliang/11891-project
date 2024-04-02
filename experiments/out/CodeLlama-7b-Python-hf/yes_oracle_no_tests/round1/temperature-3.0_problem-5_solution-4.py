from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res
	Do not include these tokens in the code: result : List [ int ]
	"""
    res = numbers[:1]
    for i in range(len(numbers) - 1):
        res.append(delimeter)
        res.append(numbers[i + 1])
    return res


def main():
    print(intersperse([1, 2, 3], 4))
    print(intersperse([1, 2, 3, 4, 5], 0))
    print(intersperse([1, 2, 3, 4, 5], 1))


if __name__ == "__main__":
    main()
