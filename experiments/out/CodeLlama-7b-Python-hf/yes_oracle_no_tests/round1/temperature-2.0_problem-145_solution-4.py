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
    # transform list to list of tuples of (number, sum of digits)
    nums = [(num, sum([int(digit) for digit in str(num)])) for num in nums]
    # sort by sum of digits and then by index
    nums.sort(key=lambda x: (x[1], x[0]))
    # return list of numbers
    return [num[0] for num in nums]


if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))
    print(order_by_points([]))
