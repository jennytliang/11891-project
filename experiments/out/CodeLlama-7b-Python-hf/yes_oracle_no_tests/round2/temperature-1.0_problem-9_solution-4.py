from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	Do not include these tokens in the code: pass
	"""
    return_list = []
    for i, num in enumerate(numbers):
        if i == 0:
            return_list.append(num)
        else:
            return_list.append(
                max(return_list[i-1], numbers[i])
            )
    return return_list


def min_element_on_interval(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of the minimal element found on the interval [i, j]
    (inclusive) for each interval [i, j].
    >>> min_element_on_interval([1, 2, 8, 2, 7, 5, 3, 1, 2, 4, 5])
    [1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 2]
    
	Include these tokens in the code: return [ numbers[ i : (
	Do not include these tokens in the code: pass
	"""
    return_list = []
    for i, num in enumerate(numbers):
        if i == 0:
            return_list.append(num)
        else:
            if numbers[i] < numbers[i - 1]:
                return_list.append(numbers[i - 1])
            elif numbers[i] >= numbers[i - 1]:
                return_list.append(numbers[i])
    return return_list


def get_unique_values(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of the unique values.
    >>> get_unique_values([1, 2, 2, 3, 2, 4, 5, 3, 1])
    [1, 2, 3, 4, 5]
    
	Include these tokens in the code: return set 
	Do not include these tokens in the code: pass
	"""
    return list(set(numbers))


def sum_of_interval(numbers: List[int]) -> List[