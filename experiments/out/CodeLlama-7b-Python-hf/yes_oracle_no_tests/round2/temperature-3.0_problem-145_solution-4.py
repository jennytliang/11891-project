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
    return sorted(nums, key=lambda x: (sum_of_digits(x), x))


def sum_of_digits(n):
    """
    Calculate the sum of digits of a given integer.
    """
    return sum([int(d) for d in str(n)])


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([-11, -12, -1, 1, 11]) == [-1, -11, -12, 1, 11]
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert order_by_points([-1, -1, -1, -1]) == [-1, -1, -1, -1]
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert order_by_points([11, 12, 13, 14, 15]) == [11, 12, 13, 14, 15]
    assert order_by_points([]) == []
    assert order_by_points([1]) == [1]
    assert order_by_points([-1]) == [-1]
    assert order_by_points([1, 2]) == [1, 2]
    assert order_by_points([-1, -2]) == [-1, -2]
    assert order_by_points([1, 2, 3]) == [1, 2, 3]
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]
    assert order_by_points([1, 2, 3, 4]) == [1, 2, 3, 4