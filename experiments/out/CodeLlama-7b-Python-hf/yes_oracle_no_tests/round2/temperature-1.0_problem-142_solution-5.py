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
    
    # we need to create a list of the squares and cubes of the list elements 
    # the elements of the list will be the index of the list 
    # the values of the list will be the elements of the list squared or cubed 
    # depending on whether the index is a multiple of 3 or 4 
    
    # we can do this by looping through the list 
    # if the index is a multiple of 3 or 4, we square or cube the element 
    # if not, we leave the element as it is 
    # then we add the squared/cubed elements to a new list 
    # we can then sum the elements in the new list to get the total sum 
    
    # create a list of the squared and cubed elements of the list 
    lst_squared_cubed = []
    
    for i in range(len(lst)):
        if i % 3 == 0:
            lst_squared_cubed.append(lst[i]**2)
        elif i % 4 == 0:
            lst_squared_cubed.append(lst[i]**3)
        else:
            lst_squared_cubed.append(lst[i])
    
    # return the sum of the squared and cubed elements 
    return sum(lst_squared_cubed)
































