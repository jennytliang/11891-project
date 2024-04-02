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
    return sorted(nums, key=lambda x: x % 10 + x // 10, reverse=True)


def order_by_points2(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points2([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points2([]) == []

    You can't use built-in sorting function.
    """
    nums = sorted(nums, key=lambda x: x % 10 + x // 10)
    for i in range(len(nums) - 1):
        if nums[i] % 10 + nums[i] // 10 == nums[i + 1] % 10 + nums[i + 1] // 10:
            while i < len(nums) - 1 and nums[i] % 10 + nums[i] // 10 == nums[i + 1] % 10 + nums[i + 1] // 10:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
    return nums


def order_by_points3(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points3([1, 11, -1, -11, -12]) == [-1, -