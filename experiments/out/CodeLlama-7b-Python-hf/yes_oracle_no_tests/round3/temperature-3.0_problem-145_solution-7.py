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
    def weight(x):
        return sum([int(i) for i in str(x)])
    return sorted(nums, key=lambda x: (weight(x), x))


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([2, 14, 3, 4, 1, 10]) == [1, 3, 4, 10, 14, 2]
    assert order_by_points([-100, -101, 100, 101]) == [-101, -100, 101, 100]
    assert order_by_points([-1000, 1000, 0]) == [0, -1000, 1000]
    assert order_by_points([-1000, 1000, 0, 1]) == [0, -1000, 1, 1000]
    assert order_by_points([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert order_by_points([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]) == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
    assert order_by_points([100, 200, 300, 400, 500, 600, 700, 800, 900]) == [100, 200, 300, 400, 500, 600, 700, 800, 900