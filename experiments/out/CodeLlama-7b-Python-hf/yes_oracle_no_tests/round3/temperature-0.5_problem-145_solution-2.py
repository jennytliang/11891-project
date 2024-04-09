def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight ( x ):
	"""
    nums_copy = nums[:]
    nums_copy.sort(key=weight)
    return nums_copy


def weight(num):
    return sum(int(x) for x in str(num))


print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))
