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
    
	Include these tokens in the code: num
	Do not include these tokens in the code: x
	'''


    count = dict()
 
    # Traverse through the list
    for i in lst:
        if i > 0:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
 
    # Traverse the list again to check frequency
    for i in lst:
        if i > 0 and count[i] >= i:
            return i
 
    return -1