def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight
	Do not include these tokens in the code: num _ sum s = [[ num
	"""
    
    nums_sorted = sorted(nums, key=lambda num: weight(num))
    return nums_sorted


def weight(num):
    num_str = str(num)
    return sum(int(i) for i in num_str)


print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))
