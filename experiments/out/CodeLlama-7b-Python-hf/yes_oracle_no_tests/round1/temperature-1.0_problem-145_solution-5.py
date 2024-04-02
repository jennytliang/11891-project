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
    return sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))


if __name__ == '__main__':
    print('Example:')
    print(order_by_points([1, 11, -1, -11, -12]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([1]) == [1]
    assert order_by_points([1, -1]) == [-1, 1]
    assert order_by_points([123, 45]) == [45, 123]
    assert order_by_points([123, 45, 0]) == [0, 123, 45]
    assert order_by_points([123, 45, 0, 0]) == [0, 0, 123, 45]
    assert order_by_points([123, 45, 0, 0, 0]) == [0, 0, 0, 123, 45]
    print('You are awesome! All tests are done! Go Check it!')
