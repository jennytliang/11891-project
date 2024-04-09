def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: # My and best way solution
	"""
    if lst == []:
        return None
    elif len(lst) == 1:
        return None
    else:
        lst.sort()
        lst = lst[1:]
        return min(lst)


def next_smallest_1(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: # My and best way solution
	"""
    if lst == []:
        return None
    elif len(lst) == 1:
        return None
    else:
        lst.sort()
        lst = lst[1:]
        return min(lst)


def next_smallest_2(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: # My and best way solution
	"""
    if lst == []:
        return None
    elif len(lst) == 1:
        return None
    else:
        lst.sort()
        lst = lst[1:]
        return min(lst)


def next_smallest_3(lst):
    """
    You are given a list of integers.
    Write a function next_smallest()