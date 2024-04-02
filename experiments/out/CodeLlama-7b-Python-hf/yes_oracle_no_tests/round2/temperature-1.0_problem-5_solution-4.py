from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: : List [ int ]
	"""

   # print("delimeter is", delimeter)
    numbers_list = list(numbers) # make sure the argument is a list
    length = len(numbers)
    if length <=1:
        return numbers
    half_length = int(length / 2)
    for i in range(half_length):
        numbers_list.insert(2*i+1,delimeter)
    return numbers_list


def intersperse_recursive(numbers: List[int], delimeter: int, counter: int = 0) -> List[int]:
    number_list = [v for v in numbers]
    return intersperse_helper(counter, number_list, delimeter)


def intersperse_helper(counter, numbers, delimeter):  # counter used for recursion
    if counter < len(numbers)-1:
        numbers.insert(2*counter+1, delimeter)
        counter += 1
        return intersperse_helper(counter, numbers, delimeter)
    return numbers


"""
if __name__ == '__main__':
    a = [1, 2, 3, 4]
    output = intersperse_recursive(a, 9)
    print(output)
"""
