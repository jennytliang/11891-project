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
    return sorted(nums, key=lambda x: (sum(list(map(int, str(x)))), x))


if __name__ == '__main__':
    print("Example:")
    print(order_by_points([1, 11, -1, -11, -12]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([-1]) == [-1]
    assert order_by_points([0]) == [0]
    assert order_by_points([1, 11, -12, -1, 12]) == [-1, -12, 1, 11, 12]
    assert order_by_points([10, 100, 1, 1000, 10000]) == [1, 10, 100, 1000, 10000]
    print("Coding complete? Click 'Check' to earn cool rewards!")
