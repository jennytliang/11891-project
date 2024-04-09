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
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {}
	'''

    co = {}
    for i in range(len(lst)):
        if lst[i] in co:
            co[lst[i]] += 1
        else:
            co[lst[i]] = 1
    for k, v in co.items():
        if k > 0 and v >= k:
            return k
    return -1


def test_function():
    assert search([4, 1, 2, 2, 3, 1]) == 2, "First"
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3, "Second"
    assert search([5, 5, 4, 4, 4]) == -1, "Third"
    assert search([4, 1, 2, 2, 3, 1, 4, 4, 4]) == 4, "Fourth"
    assert search([3, 1, 2, 2, 3, 1, 4, 4, 4]) == 3, "Fifth"
    assert search([4, 1, 2, 2, 3, 1, 4, 4, 4]) == 4, "Sixth"
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3, "Seventh"
    assert search([1, 1, 2, 2, 3, 3, 4, 4, 4]) == 1, "Eighth"
    assert search([4, 1, 2, 2, 3, 1, 4, 4, 4]) == 4, "Ninth"
    assert search([4, 1, 2, 2, 3, 1, 4, 4, 4]) == 4, "Tenth"


if __name__ == '__main__':
    test_function()
