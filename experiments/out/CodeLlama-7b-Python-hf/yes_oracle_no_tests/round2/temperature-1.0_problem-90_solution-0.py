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


    if le == len(lst)-1:
        #return None
        raise Exception("No such element")
    elif le == len(lst)-2:
        lst.remove(el)
        return lst[0]
    elif lst[le+1] < el and lst[le] <= el:
        le += 1
        return next_smallest(lst)
    elif lst[le] > el and le < (len(lst)-2):
        return next_smallest(lst)
    else:
        l_of_l = lst[le+1:]
        lst.remove(el)
        return next_smallest(lst)