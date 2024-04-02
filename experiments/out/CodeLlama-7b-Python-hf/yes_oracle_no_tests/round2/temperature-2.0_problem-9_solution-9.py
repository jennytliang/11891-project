from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return []
    max_so_far = max_till_now = numbers[0]
    result = [numbers[0]]
    for number in numbers[1:]:
        max_till_now = max(number, max_till_now + number)
        result.append(max_till_now)
    return result


def max_in_list(numbers: List[int]) -> int:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_in_list([1, 2, 3, 2, 3, 4, 2])
    4
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return 0
    max_so_far = max_till_now = numbers[0]
    for number in numbers[1:]:
        max_till_now = max(number, max_till_now + number)
    return max_till_now


def max_in_list_2(numbers: List[int]) -> int:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_in_list_2([1, 2, 3, 2, 3, 4, 2])
    4
    
	Do not include these tokens in the code: if not numbers :
	"""
    if not numbers:
        return 0
    max_so_far = max_till_now = numbers[0]
    for number in numbers[1:]:
        max_till_now, max_so_far = max(number, max_till_now + number), max(max_so_far, max_till_now)
    return max_so_far


def max_product(numbers: List[int]) -> int:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_product