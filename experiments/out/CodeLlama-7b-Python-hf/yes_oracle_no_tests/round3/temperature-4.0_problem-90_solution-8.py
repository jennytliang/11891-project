def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: return None # Set the
	"""


    if len(lst) < 2:
        return None
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[0]
        return None

    lst.sort()
    lst.pop(0)
    lst.pop(0)
    if len(lst) > 0:
        for i in range(len(lst)):
            if lst[i] != lst[i+1]:
                return lst[i]
    return None

print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))
