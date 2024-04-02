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

    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return None
    else:
        lst.sort()
        for i in range(len(lst)):
            if lst[i] <= lst[i + 1]:
                return lst[i + 1]
        return None

def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None