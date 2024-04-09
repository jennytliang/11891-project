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
    return sorted(nums, key=lambda x: weight(x))


def weight(num):
    return sum(map(int, str(num)))


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([-123456789]) == [-123456789]
    assert order_by_points([1, 2, 11, -1234, 5, 4, 3, 2, 1, 0]) == [
        0, 1, 2, 3, 4, 5, 11, -1234, 2, 1
    ]
    assert order_by_points([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ]
    assert order_by_points([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ]
    assert order_by_points([100, 101, 110, 111, 1001, 1010, 1100, 1101, 1110]) == [
        100, 101, 110, 111, 1001, 1010, 1100, 1101, 1110
    ]
    assert order_by_points([1, 2, 3, 4, 5, 6,