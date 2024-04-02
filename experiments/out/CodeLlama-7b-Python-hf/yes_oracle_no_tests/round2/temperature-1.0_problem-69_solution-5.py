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
    
	Do not include these tokens in the code: # return #
	'''
    if len(lst) > 0:
        for i in range(0, len(lst)):
            print(lst.count(lst[i]))
            if (lst[i] == lst.count(lst[i])):
                return -1
        for i in range(0, len(lst)):
            print(lst.count(lst[i]))
            if (lst.count(lst[i]) >= lst[i]):
                return lst[i]
    return -1


def test_function():
    assert search([1, 2, 3, 4]) == -1
    assert search([1, 1, 1, 1]) == -1
    assert search([4, 1, 2, 2, 3, 1]) == 2
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    assert search([5, 5, 4, 4, 4]) == -1
    assert search([3, 3, 1, 2, 1, 2, 3, 3]) == 3
    assert search([4, 1, 2, 2, 3, 1]) == 2

if __name__ == '__main__':
    test_function()