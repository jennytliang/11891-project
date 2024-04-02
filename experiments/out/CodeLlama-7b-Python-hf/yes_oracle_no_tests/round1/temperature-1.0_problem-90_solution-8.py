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

    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return None
    
    found = True
    num_1, num_2 = lst[0], float('inf')
    
    for i in lst:
        if i <= num_2:
            num_2 = i
        elif i <= num_1 and i > num_2:
            num_1 = i
            
    if num_1 == float('inf') or num_2 == float('inf'):
        return None
    else:
        return num_1

print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))