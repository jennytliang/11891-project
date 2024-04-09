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
	Do not include these tokens in the code: e
	'''

    count = dict()
  
    # Traverse through list
    for i in lst:
        if i < 0:
            continue
  
        # If number is already in the dictionary, increment its value
        if i in count:
            count[i] += 1
  
        # If number is not in the dictionary, add it
        else:
            count[i] = 1
  
    # Traverse through dictionary
    for i in count:
  
        # If value is greater than the key and greater than 0
        if count[i] >= i:
            return i
  
    # If no number meets the criteria
    return -1
