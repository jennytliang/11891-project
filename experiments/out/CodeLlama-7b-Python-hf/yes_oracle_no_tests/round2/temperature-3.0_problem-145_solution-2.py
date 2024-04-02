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
    return sorted(nums, key=lambda x: (sum(map(int, str(x))), x))


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([-10, 10]) == [-10, 10]
    assert order_by_points([-1, 1]) == [1, -1]
    assert order_by_points([1, -1]) == [1, -1]
    assert order_by_points([1, 10, 100, 1000, 10000]) == [1, 10, 100, 1000, 10000]
    assert order_by_points([10, 100, 1000, 10000, 100000]) == [10, 100, 1000, 10000, 100000]
    assert order_by_points([1, 11, 111, 1111, 11111]) == [1, 11, 111, 1111, 11111]
    assert order_by_points([11, 111, 1111, 11111, 111111]) == [11, 111, 1111, 11111, 111111]
    assert order_by_points([111, 1111, 11111, 111111, 1111111]) == [111, 1111, 11111, 111111, 1111111]
    assert order_by_points([1111, 11