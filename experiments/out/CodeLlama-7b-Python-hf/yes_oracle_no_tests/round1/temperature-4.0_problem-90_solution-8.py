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
    if len(lst) < 2: return None
    mini = lst[0]
    for i in lst:
        if i < mini: mini = i
    min_list = []
    for i in lst:
        if i < mini: min_list.append(i)
    if min_list == []: return None
    return min_list[1]
    


def test_function():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([1, 2, 1]) == 1
    assert next_smallest([1, 1, 1]) == None
    assert next_smallest([7, 7, 7]) == None
    assert next_smallest([7, 7, 6]) == 6
    assert next_smallest([7, 6, 7]) == 6
    assert next_smallest([6, 7, 7]) == 6
    assert next_smallest([0, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7]) == 3
    assert next_smallest([3, 0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == 1
    assert next_smallest([3, 1, 0, 2, 3, 3, 3, 4, 5, 6, 7]) == 0
    assert next_smallest([3, 1, 2, 0, 3, 3, 3, 4, 5, 6, 7]) == 0
    assert next_smallest([3, 1, 2, 3, 0, 3, 3, 4, 5, 6, 7]) == 0
