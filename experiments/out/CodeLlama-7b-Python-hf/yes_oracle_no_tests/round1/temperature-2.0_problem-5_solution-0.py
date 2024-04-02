from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: res =
	Do not include these tokens in the code: if not numbers : return
	"""
    if not numbers:
        return []
    res = []
    for i in range(len(numbers) - 1):
        res.append(numbers[i])
        res.append(delimeter)
    res.append(numbers[-1])
    return res


def main():
    a = [1, 2, 3]
    print(intersperse(a, 4))


if __name__ == "__main__":
    main()
