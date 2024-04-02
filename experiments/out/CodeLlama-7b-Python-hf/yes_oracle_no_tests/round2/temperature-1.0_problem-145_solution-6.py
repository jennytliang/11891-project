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
    points_list = []
    for i in range(len(nums)):
        points = sum(int(i) for i in str(nums[i]))
        points_list.append((points, i))

    return [i[0] for i in sorted(points_list)]
        

    
