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
    for i, num in enumerate(numbers):
        _list.append(max(numbers[:i + 1]))
    return _list


def max_profit(prices: List[int]) -> Tuple[int, int]:
    """ Find the maximum profit in a given sequence of prices.
    >>> max_profit([10, 5, 2, 1, 7, 3])
    (6, 4)
    
	Include these tokens in the code: return ( max ( gains ), max ( buy_days ))
	Do not include these tokens in the code: _ gains = []
	"""
    _gains = []
    _buy_days = []
    for i, num in enumerate(prices):
        if i == 0:
            _gains.append(0)
            _buy_days.append(0)
        else:
            _gains.append(prices[i] - prices[i - 1])
            _buy_days.append(i)
    return (max(_gains), _buy_days[_gains.index(max(_gains))])


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum found until given moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 5, 5, 6, 10, 12]
    
	Include these tokens in the code: return [ sum ( numbers [ :( i + 1
	Do not include these tokens in the code: _ list = []
	"""
    _list = []
    for i, num in enumerate(numbers):
        _list.append(sum(numbers[:i + 1]))
    return _list


def max_sub_array(nums: List[int]) -> Tuple[int, int, int]:
    """ Find the maximum sub-array of the given list of numbers. Return the
    **start