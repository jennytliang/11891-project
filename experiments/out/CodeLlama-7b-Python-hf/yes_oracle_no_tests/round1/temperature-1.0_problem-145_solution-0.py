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
    
    def weight(nums):
        """
        This function is to transform the integers into the sum of their digits.
        And make it into a list with the same length with the original list.
        """
        res = list(map(sum, list(str(nums))))    # str: string, int: numbers 
        return res
    
    nums = weight(nums)
    num_list = [[num, i] for i, num in enumerate(nums)]
    num_list.sort()
    
    return [num[1] for num in num_list if num[0] == num[1]]