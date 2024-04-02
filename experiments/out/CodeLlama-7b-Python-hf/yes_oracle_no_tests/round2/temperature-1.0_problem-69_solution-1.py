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
    if lst == None:
	    return -1
	count = dict ()
    greater_frequency = -1
    # loop through the list
    for item in lst:
        # check if the value in the key, exists,
        # if it does, increment it
        if (item in count):
            count[item] += 1
        elif (count[item] != 0):
            greater_frequency = item
            count[item] += 1
        # else we need to create an entry
        else:
            count[item] += 1

    # check to see if the entry is in the dictionary
    if greater_frequency in count:
        freq = count[greater_frequency]
        if freq >= greater_frequency:
            return greater_frequency
    # otherwise return -1
    return -1

search([5, 5, 4, 4, 4, 4, 5, 5, 5])