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
    
    # Create a list of 0s. The length of this list will be the same as the length of lst. 
    # The value of each entry in this list will be the sum of the squares of the values in lst.
    list_of_squares = [0] * len(lst)
    
    # Iterate through lst.
    for i in range(len(lst)):
        if i % 3 == 0:
            list_of_squares[i] = lst[i]**2
        elif i % 4 == 0:
            list_of_squares[i] = lst[i]**3
        else:
            list_of_squares[i] = lst[i]
        
    # Sum the entries of list_of_squares.
    sum_of_squares = sum(list_of_squares)
    
    return sum_of_squares
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    