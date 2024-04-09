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

    for i in range(len(nums)):
        nums[i] = (sum([int(x) for x in str(nums[i])]), nums[i])

    nums.sort(key=lambda x: x[0])

    for i in range(len(nums)):
        nums[i] = nums[i][1]

    return nums


print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))
