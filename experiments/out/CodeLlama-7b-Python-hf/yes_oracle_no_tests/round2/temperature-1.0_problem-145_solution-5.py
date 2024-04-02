def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight ( x ): x _ list
	"""
    nums.sort(key=lambda x: (-_weight(x), x))
    return nums
    

def _weight(n):
    if n > 0:
        return sum(int(x) for x in str(n))
    else:
        return -sum(int(x) for x in str(-n))
