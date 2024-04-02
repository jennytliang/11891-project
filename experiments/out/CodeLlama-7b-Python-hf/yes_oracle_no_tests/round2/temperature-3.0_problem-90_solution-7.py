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
    if len(lst) == 1:
        return None
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] <= lst[j]:
                return lst[j]

def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3
    assert next_smallest([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert next_smallest([1, 1, 1, 1, 1, 1, 1, 1, 1]) == None
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
    assert next_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 4
    assert next_smallest([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 2
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 4
    assert next_smallest([12, 