def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Include these tokens in the code: return sorted
	Do not include these tokens in the code: res = [] for i
	"""
    return sorted(arr[:k])


def minimum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the minimum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-3, -4, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [-4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [-3]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Include these tokens in the code: return sorted
	Do not include these tokens in the code: res = [] for i
	"""
    return sorted(arr[:k])


def max_profit(prices):
    """
    Given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and 
    choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot 
    achieve any profit, return 0.

    Example 1:

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                     Note that buying on day 2 and selling on day 1 is not allowed because you 
                     must buy before you sell.

    Example 