def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Do not include these tokens in the code: # Create a function which
	"""
    
    def digit_sum(num):
        return sum(int(char) for char in str(num))
    
    return sorted(nums, key=lambda x: (digit_sum(x), x))


if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))
    print(order_by_points([]))
