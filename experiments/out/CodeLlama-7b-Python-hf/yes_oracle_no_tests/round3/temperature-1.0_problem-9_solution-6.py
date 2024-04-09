from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    if len(numbers) == 0:
        return []
    max_so_far = numbers[0]
    rolling_max_numbers = [max_so_far]
    for number in numbers[1:]:
        max_so_far = max(max_so_far, number)
        rolling_max_numbers.append(max_so_far)
    return rolling_max_numbers


def get_max_profit(stock_prices: List[int]) -> Tuple[int, int]:
    """Given a list of stock prices in order, find the maximum profit that could be made by buying once 
    and selling twice (ie. buy first, then sell twice).
    
    >>> get_max_profit([5, 11, 3, 50, 60, 90])
    (89, 4)
    
    >>> get_max_profit([50, 60, 90])
    (89, 2)
    
    >>> get_max_profit([50, 50, 50])
    (0, 2)
    
    >>> get_max_profit([50, 40, 30, 20, 10])
    (0, 2)

    >>> get_max_profit([10, 20, 30, 40, 50])
    (50, 2)

    >>> get_max_profit([10, 15, 25, 30, 40])
    (30, 2)

    >>> get_max_profit([10, 11, 12, 13, 14])
    (0, 2)

    >>> get_max_profit([10, 11, 12, 13, 14, 15, 16])
    (1, 7)

    >>> get_max_profit([10, 11, 12, 13, 14, 