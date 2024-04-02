from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    for i1 in range(len(numbers)):
        for i2 in range(i1 + 1, len(numbers)):

            if abs(numbers[i1] - numbers[i2]) <= threshold:
                return True

    return False


def get_minimum_cost_to_balance(
    numbers: List[float], target_indices: List[int]
) -> int:
    """ Given a list of numbers and indices of two targets, find the minimum cost to
    balance the numbers.
    For simplicity, suppose that for target index i, all elements with index greater
    than i should be moved to the right and vice versa assuming that 0 is the most left
    and the last index is the most right.
    
    >>> get_minimum_cost_to_balance([5,1,3,4,2], [0, 4])
    2
    >>> get_minimum_cost_to_balance([2, 9, 6], [0,2])
    0
    >>> get_minimum_cost_to_balance([5,1,3,4,2,10,12], [0,4,5])
    2
    >>> get_minimum_cost_to_balance([0,9,10,3,8], [0,3])
    2
    >>> get_minimum_cost_to_balance([5, 3, 1, 2], [3, 0])
    0
    
    It must be assumed that all indexes in target_indices are in the valid range [0,
    len (numbers) ].
    It must be assumed that the indices are unique.
    """
    numbers = numbers.copy()

    numbers.sort()

    diff = (sum(numbers[0:target_indices[0] + 1]) - sum(numbers[target_indices[0] + 1:])) / 2
    if diff > 0:
        for i in range(target_indices[1] + 1, target_indices[0] + 1):
            print("adding ", abs(diff),