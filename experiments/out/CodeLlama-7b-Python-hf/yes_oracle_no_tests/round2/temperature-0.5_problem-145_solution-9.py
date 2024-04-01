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

    def weight(x):
        return sum([int(i) for i in str(x)])

    return sorted(nums, key=lambda x: (weight(x), x))


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([1, 11, -1, -11, -12, 10]) == [-1, -11, 1, -12, 10, 11]
    assert order_by_points([-100, -101, 100, 101, -1001]) == [-101, -100, -1001, 100, 101]
    assert order_by_points([-100, -101, 100, 101, -1001, 1000]) == [-100, -101, -1001, 100, 101, 1000]
    assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert order_by_points([-1, 1, -2, 2, -3, 3]) == [-3, -2, -1, 1, 2, 3]
    assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert order_by_points([