from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num
	Do not include these tokens in the code: # Your implementation here i
	"""
    num = 0
    i = 1
    
    while i < len(numbers):
        if numbers[i] == numbers[num]:
            del(numbers[i])
            
        else: 
            i +=1
            num +=1
            
    return numbers


print(remove_duplicates([1,2,3,4,5,5,5,7,8]))
# output: [1, 4, 5, 5, 5, 7, 8]

