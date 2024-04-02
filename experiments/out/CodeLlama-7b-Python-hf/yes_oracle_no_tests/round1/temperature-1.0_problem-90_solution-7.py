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

    if len(lst) < 2:
        return None

    smallest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= smallest:
            smallest = lst[i]
    if len(lst) <= 2:
        return None

    next_smallest = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < smallest and lst[i] > next_smallest:
            next_smallest = lst[i]
    return next_smallest


def test_function():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([1, 2, 1]) == 1
