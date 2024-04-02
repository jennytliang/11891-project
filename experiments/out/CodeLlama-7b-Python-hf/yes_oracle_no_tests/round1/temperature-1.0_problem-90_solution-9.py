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

    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0]
        elif lst[0] < lst[1]:
            return lst[1]
        else:
            return "no such element"

    temp = []

    for i in lst:
        for j in lst:
            if i <= j:
                temp.append(j)

    return min(temp)
