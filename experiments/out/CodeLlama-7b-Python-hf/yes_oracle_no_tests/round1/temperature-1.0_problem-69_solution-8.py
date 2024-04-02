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

    # We can make a dictionary with a count of values
    count = dict()
    found = -1
    # Loop through list
    for num in lst:
        # If value is not yet in dictionary, add with value of 1
        if num not in count:
            count[num] = 1
        else:
            # If value is already in dictionary, add by 1
            count[num] +=1
        
    # Iterate through the dictionary looking for
    # values larger than themselves and greater than
    # or equal the count of that value
    for i in range(1,max(count)):
        if count[i] >= i and i > 0:
            found = i
            break
    
    return found

# Test Cases:
print (search([4, 1, 2, 2, 3, 1])) #== 2
print (search([1, 2, 2, 3, 3, 3, 4, 4, 4])) #== 3
print (search([5, 5, 4, 4, 4])) #== -1
