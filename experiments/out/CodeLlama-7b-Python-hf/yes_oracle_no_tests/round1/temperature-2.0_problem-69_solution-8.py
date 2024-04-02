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
    
	Include these tokens in the code: count
	Do not include these tokens in the code: fre q
	'''
    return search_helper(lst, lst[0], 1)

def search_helper(lst, val, count):
    '''
    Helper function for search()
    '''
    if len(lst) == 0:
        # base case: lst is empty
        return -1
    elif val == 0:
        # base case: val is zero
        return -1
    elif lst[0] > val:
        # base case: the first element is greater than val
        return -1
    elif lst[0] == val:
        # base case: the first element is equal to val
        if count >= val:
            return val
        else:
            return search_helper(lst[1:], val, count+1)
    else:
        # recursive case
        return search_helper(lst[1:], val, count)

assert search([4, 1, 2, 2, 3, 1]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([4, 1, 2, 2, 3, 1, 2, 2, 3, 3, 3, 4, 4, 4]) == 2
assert search([1, 1, 2, 3, 4, 5]) == 3
assert search([1, 1, 2, 3, 3, 4, 5]) == 3
assert search([1, 1, 2, 3, 3, 4, 4, 5]) == 3
assert search([4, 1, 2, 2, 3, 1, 2, 2, 3, 3, 3, 4, 4, 4]) == 2
assert search([4, 1, 2, 