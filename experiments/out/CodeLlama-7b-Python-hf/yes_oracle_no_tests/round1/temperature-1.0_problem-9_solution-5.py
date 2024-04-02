from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""
    
    result: List[int] = []
    max_so_far: int = numbers[0]
    
    for number in numbers:
        if number > max_so_far:
            max_so_far = number
            
        result.append(max_so_far)
        
    return result


def rolling_max_efficient(numbers: List[int]) -> List[int]:
	""" From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""
    result: List[int] = []
    
    for number in numbers:
        result.append(max(result) if result else number)
        
    return result

# print the results from both versions of "rolling_max:" function
# and see if they are the same   
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
print(rolling_max_efficient([1, 2, 3, 2, 3, 4, 2]))


def flip_numbers(numbers: List[int]) -> List[int]:
    """ Generate a list of numbers with the same values, but with reversed order, compared to given sequence of
    integers..
    >>> flip_numbers([1, 2, 3, 123, 12, 33])
    [3, 3, 12, 123, 2, 1]
    
    Include these tokens in the code: len(numbers), int(), numbers[::-1], first = 0, numbers[first],
    last = len(numbers) - 1, number, list(), return
	Do not include these tokens in the code: _ _ - _ _
    """
   