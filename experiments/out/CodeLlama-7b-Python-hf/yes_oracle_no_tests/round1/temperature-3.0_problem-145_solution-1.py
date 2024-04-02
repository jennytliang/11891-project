def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight
	Do not include these tokens in the code: num _ sum s = [[ num
	"""
    for i in range(len(nums)):
        nums[i] = (sum([int(n) for n in str(nums[i])]), nums[i])
    nums.sort(key=lambda x: x[0])
    for i in range(len(nums)):
        nums[i] = nums[i][1]
    return nums


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([10, 1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 10, 11]
    assert order_by_points([-11, -12, 1, 11]) == [-11, -12, 1, 11]
    assert order_by_points([-11, -12, 1, 11, 10]) == [-11, -12, 1, 10, 11]
    assert order_by_points([100, 101, 110, 111]) == [100, 101, 110, 111]
    assert order_by_points([100, 101, 110, 111, 112]) == [100, 101, 110, 111, 112]
    assert order_by_points([100, 101, 110, 111, 112, 120, 121]) == [100, 101, 110, 111, 112, 120, 121]
    assert order_by_points([100, 101, 110, 111, 