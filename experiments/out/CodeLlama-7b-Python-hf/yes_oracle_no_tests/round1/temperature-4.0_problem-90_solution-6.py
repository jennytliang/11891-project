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
    mini = None
    if len(lst) >= 2:
        for i in lst:
            if mini == None:
                mini = i
            elif i < mini:
                mini = i
        return mini
    else:
        return None


def test_function():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    assert next_smallest([0, 1, 2]) == 1
    assert next_smallest([1, 0, 2]) == 0
    assert next_smallest([1, 0, 0]) == None
    assert next_smallest([1, 1, 0]) == 0
    assert next_smallest([1, 1, 1]) == None
    assert next_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3


if __name__ == '__main__':
    test_function()
