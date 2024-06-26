def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	Do not include these tokens in the code: else
	"""

    if len(lst) <= 1:
        reurn None

    lst = sorted(lst)
    return lst[1]

    # # Alternative solution
    # return sorted(lst)[1]


print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None
