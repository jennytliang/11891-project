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
    # my code:
    # def weight(x):
    #     return sum(map(int, list(str(x))))
    #
    # nums.sort(key=weight)
    # return nums

    # another solution:
    nums.sort(key=lambda x: sum(int(i) for i in str(x)))
    return nums


def order_by_points_v2(nums):
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
    # my code:
    # def weight(x):
    #     return sum(map(int, list(str(x))))
    #
    # nums.sort(key=weight)
    # return nums

    # another solution:
    nums.sort(key=lambda x: (sum(int(i) for i in str(x)), x))
    return nums


def order_by_points_v3(nums):
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