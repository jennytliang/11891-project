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
	"""


    if le(lst[0], lst[1]):
        return lst[1]
    elif le(lst[1], lst[0]):
        return lst[0]

    for i in range(2, len(lst)):
        if le(lst[i], lst[0]):
            return lst[0]
        elif le(lst[i], lst[1]):
            return lst[1]

    return None


def le(a, b):
    return a <= b


print(next_smallest([1, 2, 3, 4, 5]))
print(next_smallest([5, 1, 4, 3, 2]))
print(next_smallest([]))
print(next_smallest([1, 1]))