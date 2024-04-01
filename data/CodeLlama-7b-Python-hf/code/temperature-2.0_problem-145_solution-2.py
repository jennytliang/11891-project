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
    return [x for _, x in sorted((sum(int(i) for i in str(x)), x) for x in nums)]


if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))