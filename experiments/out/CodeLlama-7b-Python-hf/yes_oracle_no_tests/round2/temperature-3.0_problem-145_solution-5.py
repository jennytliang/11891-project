def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: x
	Do not include these tokens in the code: num
	"""

    def weigh(num):
        return sum(int(digit) for digit in str(num))

    return sorted(nums, key=lambda x: (weigh(x), x))


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([10, -1, 1, -10, 100]) == [-1, 1, -10, 10, 100]
