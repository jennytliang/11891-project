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


    if le(lst):
        return None
    if lst[0] < lst[1]:
        return lst[0]
    if lst[0] > lst[1]:
        return lst[1]
    for i in range(len(lst)):
        if i == 0:
            if lst[i] <= lst[i + 1]:
                return lst[i + 1]
        elif i == len(lst) - 1:
            if lst[i] <= lst[i - 1]:
                return lst[i - 1]
        else:
            if lst[i] <= lst[i - 1] and lst[i] <= lst[i + 1]:
                return lst[i]
    return None


def le(lst):
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return False
    if lst[0] <= lst[1]:
        return le(lst[1:])
    return False


def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
    assert next_smallest([2, 1, 3, 4, 5]) == 1
    assert next_smallest([5, 4, 3, 2, 1]) == 2
