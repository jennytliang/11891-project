def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: x
	Do not include these tokens in the code: num s
	"""

    
    dct = {}
    
    for i in range(len(nums)):
        add = nums[i]
        
        while add>0:
            
            add = add//10 + add%10
            
        if add == 0:
            add = 1

        dct[nums[i]] = nums[i] + add**2
        

    # sorting the dict based on keys in ascending order with reverse = True gives sorted in descending order, thus dividing by -1
    return list(sorted(dct.keys(),key = lambda x: -dct[x]))
    
    