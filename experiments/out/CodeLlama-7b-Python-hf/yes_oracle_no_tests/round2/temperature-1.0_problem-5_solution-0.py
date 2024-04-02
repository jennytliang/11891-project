from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: : List [ int ]
	"""

  
    if numbers != []:
        output = [numbers[0]]
        index = 1
        while index < len(numbers):
            output.append(delimeter)
            output.append(numbers[index])
            index += 1
    else:
        output = []
    
    
    return output
    

    pass


def main():
    numbers = [1, 2, 3, 4, 5]
    delimeter = 0
    result = intersperse(numbers, delimeter)

    if intersperse(numbers, delimeter) == [1, 0, 2, 0, 3, 0, 4, 0, 5]:
        print("Test passed")
    else:
        print("Test failed")
    
    result = intersperse([], 1)

    if intersperse([], 1) == []:
        print("Test passed")
    else:
        print("Test failed")
    

if __name__ == '__main__':
    main()
