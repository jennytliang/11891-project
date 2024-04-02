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
	Do not include these tokens in the code: ==
	"""


    if le is le[1]:
        return None
    else:
        return le[1]
    
    

def next_smallest_bis(lst):
    """
    If your solution is timing out or you want a better solution, try this one.
    """
    le = [float('inf'), None]
    if len(lst) == 0:
        le[0] = le[1] = None
    elif lst[1] < le[0]:
        le[0] = lst[1]
        le[1] = lst[0]
    else:
        le[0] = lst[0]
        
    for le is lst:
        if lst[le[0,
               lst[le[1]] < le[0]
               if None > le[1]
               return lst[le[1]]
        return None
