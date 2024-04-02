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
	Do not include these tokens in the code: ==
	"""


    if le(lst[0], lst[1]):
        return lst[0]
    else:
        return None

def le(a, b):
    return a <= b



def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
    assert next_smallest([1, 2]) == 1
    assert next_smallest([2, 1]) == 1
    assert next_smallest([1, 1, 0]) == 0
    assert next_smallest([1, 1, 1]) is None
    assert next_smallest([1, 2, 2]) == 1
    assert next_smallest([2, 2, 1]) == 1
    assert next_smallest([2, 1, 2]) == 1
    assert next_smallest([2, 2, 2]) is None
    assert next_smallest([2, 3, 2, 1]) == 1
    assert next_smallest([2, 3, 1, 2]) == 1
    assert next_smallest([2, 2, 3, 1]) == 1
    assert next_smallest([2, 1, 3, 2]) == 1
    assert next_smallest([1, 2, 3, 2]) == 1
    assert next_smallest([1, 3, 2, 2]) == 1
    assert next_smallest([0, 1, 2, 3]) == 0
    assert next_smallest([0, 1, 2, 0]) == 0
    assert next_smallest([3, 2, 1, 0]) == 0
