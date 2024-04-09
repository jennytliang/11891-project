def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # Your code here
	"""
    return sorted(lst)[1] if len(lst) > 1 else None


def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([1, 2, 3, 4, 5, 6, 0]) == 3
    assert next_smallest([1, 2, 3, 4, 5, 6, 7]) == 3
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8]) == 3
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
