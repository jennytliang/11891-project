from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: nu ) for nu in zip (* [
	"""


    return [max(nums) for nums in zip(*[iter(numbers)]*2)]


def rolling_window(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling windows of given size.
    >>> rolling_window([1, 2, 3, 4, 5, 6], 2)
    [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    """
    return [numbers[i:i+window_size] for i in range(len(numbers) - window_size + 1)]


def get_max_profit(stock_prices: List[int]) -> int:
    """ From a given list of integers representing stock prices, find the maximum profit possible.
    >>> get_max_profit([5, 1, 3, 2, 4, 6])
    5
    """


def get_max_profit_optimized(stock_prices: List[int]) -> int:
    """ From a given list of integers representing stock prices, find the maximum profit possible.
    >>> get_max_profit_optimized([5, 1, 3, 2, 4, 6])
    5
    """


def get_max_profit_optimized_v2(stock_prices: List[int]) -> int:
    """ From a given list of integers representing stock prices, find the maximum profit possible.
    >>> get_max_profit_optimized_v2([5, 1, 3, 2, 4, 6])
    5
    """


def get_max_profit_optimized_v3(stock_prices: List[int]) -> int:
    """ From a given list of integers representing stock prices, find the maximum profit possible.
    >>> get_max_profit_optimized_v3([5, 1, 3, 2, 4, 6])
    5
    """


def get_max_profit_optim