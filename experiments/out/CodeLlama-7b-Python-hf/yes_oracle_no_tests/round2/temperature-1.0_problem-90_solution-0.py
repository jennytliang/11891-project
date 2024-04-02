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


    if le(min(lst), lst[0]):
        return None
    else:
        return min(lst)

def le(a, b):
    return a <= b

next_smallest([1, 2, 3, 4, 5])
next_smallest([5, 1, 4, 3, 2])
next_smallest([])
next_smallest([1, 1])