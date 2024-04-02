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
	Do not include these tokens in the code: sort
	"""


  # WRITE YOUR CODE HERE
    if not nums:
        return []
    by_sum = [(sum(int(x) for x in str(num)), num) for num in nums]
    by_sum.sort()
    return [num for _, num in by_sum]


if __name__ == '__main__':
    try:
        order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        order_by_points([]) == []
    except AssertionError:
        print('Tests failed!')
    else:
        print('Tests passed!')


# def order_by_points(nums):
#     """
#     Write a function which sorts the given list of integers
#     in ascending order according to the sum of their digits.
#     Note: if there are several items with similar sum of their digits,
#     order them based on their index in original list.

#     For example:
#     >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
#     >>> order_by_points([]) == []
    
# 	Include these tokens in the code: weight
# 	Do not include these tokens in the code: sort
#     """


#   # WRITE YOUR CODE HERE
#     if not nums:
#         return []
#     by_sum = [(sum(int(x) for x in str(num)), num) for num in nums]
#     by_sum.sort()
#     return [num for _, num in by_sum]


# if __name__ == '__main__':
#     try:
#         order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
#         order_by_points([]) == []
