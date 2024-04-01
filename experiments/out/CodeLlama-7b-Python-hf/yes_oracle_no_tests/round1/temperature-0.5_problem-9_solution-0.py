from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""

    
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for number in numbers[1:]:
        if number > max_so_far:
            max_so_far = number
        result.append(max_so_far)
        
    return result


def rolling_max_one_liner(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""
    
    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def find_three_largest_numbers(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, return a tuple of three largest integers found in the sequence.
    >>> find_three_largest_numbers([1, 3, 4, 5, 2, 7, 7, 8, 9, 15, 12])
    (15, 12, 8)
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _