def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: # First we check if the list
	"""

    def next_smallest(lst):
        if len(lst) < 2:
            return None

        lst.sort()

        return lst[1]

    return next_smallest(lst)


print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))
