def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: len
	Do not include these tokens in the code: le ( min
	"""


    if len(lst) == 0:
        return None
    
    mins = sorted(lst)[1]
    for i in range(len(lst)):
        if lst[i] == mins:
            return lst[i+1]
            
    return None













































