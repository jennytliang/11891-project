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
    for num in nums:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
    
    # Sort the list first by sum of digits, then by index
    return sorted(nums, key=lambda x:(sum_digits(x), x))
    
def sum_digits(n):
    return sum(int(d) for d in str(n))