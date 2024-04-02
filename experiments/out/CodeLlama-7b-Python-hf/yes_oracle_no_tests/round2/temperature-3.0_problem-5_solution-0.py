from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: []
	Do not include these tokens in the code: [ numbers [ 0 ]]
	"""


    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
        else:
            result.append(delimeter)
            result.append(numbers[i])
    return result


# def main():
#     print(intersperse([], 4))
#     print(intersperse([1, 2, 3], 4))

# if __name__ == "__main__":
#     main()
