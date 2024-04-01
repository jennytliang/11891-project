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
    num_sums = [[num, sum(int(x) for x in str(num))] for num in nums]

    num_sums.sort(key=lambda x: (x[1], nums.index(x[0])))
    return [x[0] for x in num_str]