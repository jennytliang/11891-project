from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _ max _ list : List
	"""
    max_list = []
    for i in range(len(numbers)):
        max_element = max(numbers[0:i+1])
        max_list.append(max_element)
    return max_list


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (element, maximum element found until given
    moment in the sequence).
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 2), (3, 3), (2, 3), (3, 3), (4, 4), (2, 4)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _ max _ tuple : List
	"""
    max_list = []
    for i in range(len(numbers)):
        max_element = max(numbers[0:i+1])
        max_list.append((numbers[i], max_element))
    return max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 1, 2, 2, 2]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _ min _ list : List
	"""
    min_list = []
    for i in range(len(numbers)):
        min_element = min(numbers[0:i+1])
        min_list.append(min_element)
    return min_list


def rolling_min_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples (