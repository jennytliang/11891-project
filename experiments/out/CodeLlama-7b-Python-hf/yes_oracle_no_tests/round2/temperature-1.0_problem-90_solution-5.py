def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: <
	"""


    if le == 1:
        return None
    if le == 2:
        return 2
    i = 0
    while i < len(lst):
        if lst[i] >= lst[i - 1] and lst[i] <= lst[i - 2] and lst[i] != le - 1 and lst[i] != 1:
            return lst[i]
        i += 1
    return None