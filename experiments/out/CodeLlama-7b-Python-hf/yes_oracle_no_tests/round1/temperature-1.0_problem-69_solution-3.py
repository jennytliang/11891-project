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
    return __result_search(lst, True)

def frequencies(lst):
    '''
    Return the list of unique frequencies in the given list.
    The return value should be sorted in ascending order.
    Example: frequencies([1, 1, 2, 4, 4, 3, 4, 5]) == [1, 2, 3, 4, 5]
    Examples count
    Count number of repeated values in the given list. Lists are not unique, you can use "set" data structure instead.
    Examples:
        repeated([4, 1, 2, 1, 4]) == 1
        repeated([3, 2, 2, 3, 4, 3, 0, 3]) == 3
	
    include in code: count = dict ()
    '''
    return __result_search(lst, False)
    
        
def __result_search(lst, to_return):
    result = []
    count = {}
    for elem in lst:
        count[elem] = count.get(elem, 0) + 1
    if to_return: 
        return max(count)
    else:
        return list(count.keys())