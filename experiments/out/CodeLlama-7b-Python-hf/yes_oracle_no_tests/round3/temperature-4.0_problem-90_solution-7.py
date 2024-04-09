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

    if len(lst) < 2:
        return None
    else:
        smallest = lst[0]
        smallest_index = 0
        for i in range(len(lst)):
            if lst[i] < smallest:
                smallest = lst[i]
                smallest_index = i
        lst.pop(smallest_index)
        return lst[0]


def test_function():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([1, 2, 3, 4, 3, 2, 1]) == 2
    assert next_smallest([1, 2, 0, 3, 4, 3, 2, 1]) == 0
    assert next_smallest([1, 2, 3, 4, 5, 6]) == 3
    assert next_smallest([6, 5, 4, 3, 2, 1]) == 2
    assert next_smallest([1, 1, 0, 0, 0]) == None
