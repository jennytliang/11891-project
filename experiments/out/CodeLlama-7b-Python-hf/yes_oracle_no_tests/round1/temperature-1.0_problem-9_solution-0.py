from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    rolling_max_list = []
    max_so_far = numbers[0]
    for number in numbers:
        if number > max_so_far:
            max_so_far = number
        rolling_max_list.append(max_so_far)
    return rolling_max_list


def max_profit(stock_prices: List[int]) -> int:
    """ Finds the max profit that can be made by buying and selling a stock only once.
    >>> max_profit([9, 11, 8, 5, 7, 10])
    5
    
	Do not include these tokens in the code: max_profit profit = stock_prices
	"""
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - min_price
    for price in stock_prices[1:]:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


def max_profit_dp(stock_prices: List[int]) -> int:
    """ Finds the max profit that can be made by buying and selling a stock only once.
    >>> max_profit_dp([9, 11, 8, 5, 7, 10])
    5
    
	Do not include these tokens in the code: max_profit profit = stock_prices
	"""
    min_price = stock_prices[0]
    max_profit = 0
    for price in stock_prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


def max_profit_greedy(stock_prices: List[int]) -> int:
    """ Finds the max profit that can be made by buying and selling a stock only once.
   