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
    
	Do not include these tokens in the code: # counting the frequency of each
	'''


    count = 0
    for i in range(len(lst)):
        if lst[i] in lst[i+1:]:
            count += 1
        else:
            count = 0
        if lst[i] > 0 and count >= lst[i]:
            return lst[i]
    return -1