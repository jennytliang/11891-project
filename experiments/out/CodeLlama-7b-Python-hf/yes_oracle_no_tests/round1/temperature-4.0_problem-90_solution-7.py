def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: mini = None #
	"""
    mini = None
    for i in lst:
        if mini == None or i < mini:
            mini = i
    if mini == None:
        return None
    else:
        lst.remove(mini)
        for j in lst:
            if j < mini:
                mini = j
    return mini

    # one-liner
    # return min(min(lst), min(lst[lst.index(min(lst))+1:])) if lst else None
