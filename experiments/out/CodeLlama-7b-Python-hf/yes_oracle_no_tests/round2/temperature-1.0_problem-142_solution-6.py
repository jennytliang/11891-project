def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    
	Do not include these tokens in the code: This function will take a list of
	"""
    
    # create a variable to hold the sum of the entries
    sum = 0
    # loop through the list
    for i in range(len(lst)):
        # if the index is a multiple of 3, square the entry
        if i % 3 == 0:
            sum += lst[i]**2
        # if the index is a multiple of 4, cube the entry
        elif i % 4 == 0:
            sum += lst[i]**3
        # if the index is neither multiple of 3 or 4, do not change the entry
        else:
            sum += lst[i]
    # return the sum of the entries
    return sum