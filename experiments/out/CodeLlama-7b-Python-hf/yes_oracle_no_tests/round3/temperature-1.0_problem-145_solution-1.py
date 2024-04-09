def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Do not include these tokens in the code: # [ 1 , 1 1
	"""
    return sorted(nums, key=lambda n: sum(int(c) for c in str(n)), reverse=True)


if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))
