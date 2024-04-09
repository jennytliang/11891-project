def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: weight
	Do not include these tokens in the code: get _ points
	"""

   # pass

    # create a new list of tuples, each tuple containing the number and its sum of digits
    nums_and_sums = [(num, sum(int(digit) for digit in str(num))) for num in nums]

    # sort the list of tuples according to the second element (sum of digits)
    nums_and_sums_sorted = sorted(nums_and_sums, key=lambda x: x[1])

    # return the sorted list of numbers
    return [num for num, _ in nums_and_sums_sorted]


print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))
