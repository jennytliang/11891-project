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
    if len(nums) == 0:
        return []
    
    # compute weights for each num
    weights = [sum([int(s) for s in str(elem)]) for elem in nums]
    # sort based on weight, then index
    return [elem for _, elem in sorted(zip(weights,nums))]

    