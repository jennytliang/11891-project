def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len
	Do not include these tokens in the code: def check _ small
	"""
    pass

def next_smallest_2(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len
	Do not include these tokens in the code: def check _ small
	"""
    # pass
    # if len(lst) == 0:
    #     return None
    # if len(lst) == 1:
    #     return None
    # if len(lst) == 2:
    #     return lst[1]
    # if lst[0] < lst[1]:
    #     return lst[1]
    # if lst[0] > lst[1]:
    #     return None
    # if lst[0] == lst[1]:
    #     for num in lst:
    #         if lst[0] > num:
    #             return num
    #     return None
    
    for num in lst:
        if lst[0] > num:
            return num
    return None

def next_smallest_3(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len
	Do not include these tokens in the code: def check _