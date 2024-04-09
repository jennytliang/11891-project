from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: result = [] current _
	"""
    result = []
    current_max = None
    for number in numbers:
        if current_max is None or number > current_max:
            current_max = number
        result.append(current_max)
    return result


def max_contiguous_sum(sequence: List[int]) -> int:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> max_contiguous_sum([1, 2, 3, 2, 3, 4, 2])
    10
    
	Include these tokens in the code: result = 0 _
	"""
    result = 0
    current_max = 0
    for number in sequence:
        current_max = max(current_max + number, number)
        result = max(result, current_max)
    return result


def knapsack(items: List[Tuple[int, int]], capacity: int) -> int:
    """ Find a subset of items with maximal total value, so that its size does not exceed the capacity.
    >>> knapsack([(10, 2), (12, 2), (11, 3), (13, 4), (15, 3), (11, 1), (12, 1)], 5)
    39
    
	Include these tokens in the code: result = 0 _
	"""
    result = 0
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)  # sort by ratio value/weight
    for item in items:
        if capacity - item[1] >= 0:
            capacity -= item[1]
            result += item[0]
        else:
            result += capacity / item[1] * item[0]
            break
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
