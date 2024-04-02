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
    # Make a dictionary counting keys appearance of number
    if not lst:
        return -1
    count = {}
    for i in lst:
        count[i] = count.get(i, 0) + 1
    # Search in it and return key
    try:
        max_item = max(count.keys(), key=lambda k: (count.get(k) >= k, -k))
    except:
        return -1
    return max_item
