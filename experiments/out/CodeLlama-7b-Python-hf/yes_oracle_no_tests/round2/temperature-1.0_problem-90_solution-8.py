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


    if leq_count(lst) == 0:
        return None
    else:
        return find_first_geq(lst, lst[0])

def leq_count(lst):
    """
    Returns the number of elements in lst that are less than or equal to lst[0]
    """
    return sum(1 for i in lst if i <= lst[0])

def find_first_geq(lst, val):
    """
    Returns the first element in lst that is greater than or equal to val.
    If no such element exists, return None.
    """
    for i in lst:
        if i >= val:
            return i
    return None



































































































