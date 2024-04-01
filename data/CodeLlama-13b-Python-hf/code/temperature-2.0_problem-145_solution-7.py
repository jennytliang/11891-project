def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # END OF CONTEXT
    pass
    # END OF SOLUTION


def check(candidate):
    assert candidate([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert candidate([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]