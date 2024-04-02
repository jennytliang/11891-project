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


    if le(max(lst), min(lst)):
        return None
    new_lst = lst
    first = min(lst)
    new_lst.remove(first)
    second = min(new_lst)

    return second

def le(a, b):
    return a <= b
