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
    result = -1
    count = {}
    for num in lst:
        if not num in count:
            count[num] = 1
        else:
            count[num] += 1
            
    maxValue = max(count)
    for key, value in count.items():
        if key > 0 and value > key:
            return(key)
    return(result)