from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: i
	Do not include these tokens in the code: num
	"""


    res = []
 
    for i in range(len(numbers)):
        res.append(numbers[i])
        res.append(delimeter)
    return res[:-1]


def main():
    print('***Intersperse***')
    print(intersperse([1, 2, 3], 4))
    print(intersperse([], 4))


if __name__ == '__main__':
    main()
