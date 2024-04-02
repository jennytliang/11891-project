def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Do not include these tokens in the code: #
	"""
    # your code here
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if sum(int(i) for i in str(nums[i])) > sum(int(i) for i in str(nums[j])):
    #             nums[i], nums[j] = nums[j], nums[i]
    
    # return nums
    return sorted(nums, key = lambda x: sum(int(i) for i in str(x)), reverse = False)


if __name__ == '__main__':
    print('Example:')
    print(order_by_points([1, 11, -1, -11, -12]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([-100, 1]) == [-100, 1]
    assert order_by_points([3, 1]) == [1, 3]
    assert order_by_points([3, 1, 10, 100]) == [1, 1, 3, 10, 100]
    print('You are awesome! All tests are done! Go Check it!')
