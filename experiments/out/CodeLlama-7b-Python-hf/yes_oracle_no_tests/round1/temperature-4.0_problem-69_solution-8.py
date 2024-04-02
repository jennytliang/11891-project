def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: count = dict ()
	'''
    count = {}
    for i in lst:
        try:
            count[i] += 1
        except KeyError:
            count[i] = 1
    for i in lst:
        if count[i] >= i and i > 0:
            return i
    return -1


def test_search():
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([5, 5, 4, 4, 4, 1, 1, 1, 1]) == 5
    assert search([5, 5, 4, 4, 4, 1, 1, 1, 1, 0]) == 5
    assert search([]) == -1
    assert search([-1]) == -1
    assert search([-1, -1]) == -1
    assert search([0]) == -1
    assert search([0, 0]) == -1
    assert search([0, 1]) == 1
    assert search([1, 1]) == 1
    assert search([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
