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
    # return sorted(nums, key=lambda x: sum([int(i) for i in str(x)]))
    # return sorted(nums, key=lambda x: sum([int(i) for i in str(x)]))
    
    # return sorted(nums, key=lambda x: (sum([int(i) for i in str(x)]), nums.index(x)))
    # return sorted(nums, key=lambda x: (sum([int(i) for i in str(x)]), nums.index(x)))
    # return sorted(nums, key=lambda x: (sum([int(i) for i in str(x)]), nums.index(x)))
    return sorted(nums, key=lambda x: (sum([int(i) for i in str(x)]), nums.index(x)))


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([1, -1]) == [-1, 1]
    assert order_by_points([-2, -1, 0, 1, 2]) == [-2, -1, 0, 1, 2]
    assert order_by_points([2, 1, 2, 1]) == [1, 1, 2, 2]
    assert order_by_points([2, 1, 2, 1]) == [1, 1, 2, 2]
    assert order_by_points([2, 1, 3, 1]) == [1, 1, 3, 2]
    assert order_by_points([0, 1, 0, 1]) == [0, 0, 1, 1]
    assert order_by_points([1, -1]) == [-1, 1]
    assert order_by_points([1, 2, 3, 4]) == [1, 2, 3, 4]