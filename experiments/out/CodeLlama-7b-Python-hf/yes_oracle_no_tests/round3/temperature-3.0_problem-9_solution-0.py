from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	Do not include these tokens in the code: _ list = []
	"""
    _list = []
    for i in range(len(numbers)):
        _list.append(max(numbers[:i + 1]))
    return _list


def max_subarray(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, generate a tuple of the sum of the maximum subarray found in the sequence.
    >>> max_subarray([1, 2, 3, -1, 4, 5, 2, 3, 6])
    (12, 3, 6)
    
	Include these tokens in the code: return (sum ( numbers [ best_start:best_end + 1]), best_start, best_end)
	Do not include these tokens in the code: _ best_start = 0
											_ best_end = 0
	"""
    _best_start = 0
    _best_end = 0
    _sum = 0
    for i in range(len(numbers)):
        if _sum < 0:
            _sum = 0
            _best_start = i
        _sum += numbers[i]
        _best_end = i
    return _sum, _best_start, _best_end


def max_subarray_v2(numbers: List[int]) -> Tuple[int, int, int]:
    """ From a given list of integers, generate a tuple of the sum of the maximum subarray found in the sequence.
    >>> max_subarray_v2([1, 2, 3, -1, 4, 5, 2, 3, 6])
    (12, 3, 6)
    
	Include these tokens in the code: return (sum ( numbers [ best_start:best_end + 1]), best_start, best_end)
	Do not include these tokens in the code: _ best_start = 0
											_ best_end = 0
	"""
    _best_start = 0
    _best_end = 