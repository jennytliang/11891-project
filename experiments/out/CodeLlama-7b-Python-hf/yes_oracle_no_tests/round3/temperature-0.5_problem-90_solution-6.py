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
	Do not include these tokens in the code: le q _ count
	"""


    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]


next_smallest([1, 2, 3, 4, 5])
next_smallest([5, 1, 4, 3, 2])
next_smallest([])
next_smallest([1, 1])