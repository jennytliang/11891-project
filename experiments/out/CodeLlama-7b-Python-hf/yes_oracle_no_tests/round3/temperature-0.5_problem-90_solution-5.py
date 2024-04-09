def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len ( lst ) <= 1 : return
	"""
    if len(lst) <= 1:
        return None
    # create a set of the list to remove duplicates
    lst_set = set(lst)
    # create a list of the set to sort it
    lst_list = list(lst_set)
    lst_list.sort()
    return lst_list[1]


def next_smallest_1(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len ( lst ) <= 1 : return
	"""
    if len(lst) <= 1:
        return None
    # create a set of the list to remove duplicates
    lst_set = set(lst)
    # create a list of the set to sort it
    lst_list = list(lst_set)
    lst_list.sort()
    return lst_list[1]


def next_smallest_2(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len ( lst ) <= 1 : return
	"""
    if len(lst) <= 1:
        return None
    # create a set of the list to remove duplicates
   