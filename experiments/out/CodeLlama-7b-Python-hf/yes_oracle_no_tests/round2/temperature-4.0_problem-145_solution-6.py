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
    # def weight(x):
    #     return sum(int(i) for i in str(x))

    # return sorted(nums, key=weight)

    def weight(x):
        return sum([int(i) for i in str(x)])

    return sorted(nums, key=weight)


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([10, 100, 1000]) == [10, 100, 1000]
    assert order_by_points([-1, -11, -12, -100, -10]) == [-1, -10, -11, -12, -100]
    assert order_by_points([0, -10, -1]) == [-1, -10, 0]
    assert order_by_points([]) == []
    assert order_by_points([1,1,1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1,1,1]
    assert order_by_points([1, 11, -1, -11, 155, 155]) == [-1, 1, -11, 11, 155, 155]
    assert order_by_points([10, 100, 1000]) == [10, 100, 1000]
