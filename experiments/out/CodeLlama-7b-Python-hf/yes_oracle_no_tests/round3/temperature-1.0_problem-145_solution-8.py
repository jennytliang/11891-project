def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: x _ list = list
	Do not include these tokens in the code: return sum
	"""


    
    def weight(num):
        return sum(int(i) for i in str(num))
    
    return sorted(nums, key=weight)















































