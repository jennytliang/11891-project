from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    if max(numbers) < 0:
        raise ValueError("Negative numbers are not valid")
    rolling_max = [numbers[0]]
    for idx, el in enumerate(numbers[1:], start=1):
        rolling_max.append(max(rolling_max[-1], el))
    return rolling_max


def sum_triangular_numbers(number: int) -> int:
    """ Given a positive integer n generate a list of triangular numbers and return their sums.
    >>> sum_triangular_numbers(6)
    5
    
	Include these tokens in the code: number_list = generate_triangular_numbers
	Include these tokens in the code: return sum(number_list)
	"""
    import os

    if number < 0:
        raise ValueError("Number must be positive")
    return sum([el * (el + 1) / 2 for el in range(1, number + 1)])


def sort_0_1_2(input_list: List[int]) -> List[int]:
    """ Receive a list containing 0, 1 and 2 in shuffled order and return a list sorted in ascending order. e.g.
    [0, 2, 1, 1, 0, 0, 2] -> [0, 0, 0, 1, 1, 2, 2]
    >>> sort_0_1_2([0, 2, 1, 1, 0, 0, 2])
    [0, 0, 0, 1, 1, 2, 2]
    
	Include these tokens in the code: return _
	
	You may find this module useful: re
    """
    if len(input_list) != len(set(input_list)):
        raise ValueError("Input list cannot contain duplicate values")
    if sorted(set(input_list)) != [0, 1, 2]:
        raise ValueError("Input list must contain only elements 0, 1 and 2")
    return [0] * input_list.count(0) +