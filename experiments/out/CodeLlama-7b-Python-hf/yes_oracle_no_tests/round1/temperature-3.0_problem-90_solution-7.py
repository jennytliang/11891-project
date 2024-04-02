def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if len
	Do not include these tokens in the code: def check _ small
	"""
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]


def next_smallest_2(lst):
    min_val = min(lst)
    for val in lst:
        if val > min_val:
            return val
    return None


print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))
print(next_smallest([1, 2, 3, 4, 5, 10]))
print(next_smallest([-1, -2, -3, -4, -5]))
print(next_smallest([-1, -2, -3, -4, -5, 10]))
