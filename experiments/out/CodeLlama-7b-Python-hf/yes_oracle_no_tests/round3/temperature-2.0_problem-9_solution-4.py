from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    if not numbers:
        return []
    rolling_max_numbers = [numbers[0]]
    for i, n in enumerate(numbers[1:]):
        rolling_max_numbers.append(max(rolling_max_numbers[-1], n))
    return rolling_max_numbers


def max_profit(prices: List[int]) -> Tuple[int, int]:
    """
    >>> max_profit([7, 1, 5, 3, 6, 4])
    (5, 5)
    >>> max_profit([7, 6, 4, 3, 1])
    (-1, -1)
    >>> max_profit([1, 2, 3, 4, 5])
    (4, 4)
    """
    if not prices:
        return -1, -1
    min_price = prices[0]
    max_profit_local = 0
    max_profit_global = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        max_profit_local = max(price - min_price, max_profit_local)
        max_profit_global = max(max_profit_local, max_profit_global)
    return max_profit_global, max_profit_local


def max_profit_with_fees(prices: List[int], fee: int) -> Tuple[int, int]:
    """
    >>> max_profit_with_fees([1, 3, 2, 8, 4, 9], 2)
    (8, 7)
    >>> max_profit_with_fees([1, 3, 7, 5, 10, 3], 3)
    (6, 4)
    >>> max_profit_with_fees([1, 3, 2, 8, 4, 9], 3)
    (5, 4)
    >>> max_profit_with_fees([1