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

    # create a list to hold the squared/cubed values
    sum_of_squares = []

    # loop through the list
    for i in range(0,len(lst)):

        # if the index is a multiple of 3
        if i % 3 == 0:
            # square the value in the list
            sum_of_squares.append(lst[i]**2)
        # if the index is a multiple of 4
        elif i % 4 == 0:
            # cube the value in the list
            sum_of_squares.append(lst[i]**3)
        else:
            # append the value in the list to the list
            sum_of_squares.append(lst[i])

    # return the sum of the list
    return sum(sum_of_squares)


# test the function
lst = [1,2,3]
print(sum_squares(lst))