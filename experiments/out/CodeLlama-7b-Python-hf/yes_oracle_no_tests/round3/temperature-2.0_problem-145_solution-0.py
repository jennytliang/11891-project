def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Do not include these tokens in the code: # my code : #
	"""
    def key(x):
        return sum(map(int, str(x))), x
    return sorted(nums, key=key)


if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))
    print(order_by_points([]))
    print(order_by_points([1, 2, 3]))
    print(order_by_points([1, 3, 2]))
    print(order_by_points([1, 2, 3, 4]))
    print(order_by_points([1, 2, 3, 4, 5]))
    print(order_by_points([1, 2, 3, 4, 5, 6]))
    print(order_by_points([1, 2, 3, 4, 5, 6, 7]))
