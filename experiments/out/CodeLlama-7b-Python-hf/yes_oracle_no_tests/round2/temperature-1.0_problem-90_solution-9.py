def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 2
	"""


    if len(ls) < 2:
        return None
    
    sorted_list = sorted(lst)
    
    for i in range(len(lst)):
        if sorted_list[i] == lst[i]:
            if i == len(lst) - 1:
                return None
            if i == len(lst) - 2:
                return sorted_list[i + 1]
            if sorted_list[i + 1] != lst[i + 1]:
                return sorted_list[i + 1]
