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
	Do not include these tokens in the code: if not num s :
	"""

    # your code here
    sorted_list = sorted(nums, key=lambda x: sum(int(y) for y in str(x)))

    return sorted_list


if __name__ == '__main__':
    example1 = [1, 11, -1, -11, -12]
    actual1 = [-1, -11, 1, -12, 11]
    expected1 = order_by_points(example1)
    assert expected1 == actual1, "Expected {}, got {}".format(actual1, expected1)

    example2 = []
    actual2 = []
    expected2 = order_by_points(example2)
    assert expected2 == actual2, "Expected {}, got {}".format(actual2, expected2)
