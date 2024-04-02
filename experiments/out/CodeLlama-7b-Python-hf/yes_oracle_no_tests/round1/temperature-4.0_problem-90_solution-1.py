def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: mini = None #
	"""

    # My and best way solution
    mini = None
    if len(lst) > 2:
        lst.sort()
        mini = lst[1]
    return mini


# Best way solution
def next_smallest_best(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Do not include these tokens in the code: mini = None #
	"""

    mini = None
    if len(lst) > 2:
        mini = min(lst[1:])
    return mini


print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))
print(next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("-" * 25)

print(next_smallest_best([1, 2, 3, 4, 5]))
print(next_smallest_best([5, 1, 4, 3, 2]))
print(next_smallest_best([]))
print(next_smallest_best([1, 1]))
print(next_smallest_best([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
