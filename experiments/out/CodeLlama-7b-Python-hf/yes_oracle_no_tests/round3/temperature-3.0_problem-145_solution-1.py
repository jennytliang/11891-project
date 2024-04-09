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
	"""
    # your code here
    def weight(x):
        return sum(int(i) for i in str(x))

    nums.sort(key=weight)
    return nums


if __name__ == '__main__':
    print("Example:")
    print(order_by_points([1, 11, -1, -11, -12]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([-10, -10]) == [-10, -10]
    assert order_by_points([10, 10]) == [10, 10]
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    print("Coding complete? Click 'Check' to earn cool rewards!")
