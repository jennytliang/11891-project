def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def
	Do not include these tokens in the code: num s . sort ( key
	"""
    
    def get_points(num):
        points = 0
        for digit in str(num):
            points += int(digit)
        return points
    
    return sorted(nums, key=lambda x: (get_points(x), x))


print(F"order_by_points.py: order_by_points([1, 11, -1, -11, -12]) = {order_by_points([1, 11, -1, -11, -12])}")
print(F"order_by_points.py: order_by_points([]) = {order_by_points([])}")
