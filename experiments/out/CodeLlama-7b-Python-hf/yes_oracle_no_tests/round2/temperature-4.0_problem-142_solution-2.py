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
    
    # Initialize variables
    square_sum = 0
    cube_sum = 0
    
    # Iterate through the list
    for i, num in enumerate(lst):
        # Square the number if index is a multiple of 3
        if i % 3 == 0:
            square_sum += num ** 2
        # Cube the number if index is a multiple of 4 and not a multiple of 3
        elif i % 4 == 0:
            cube_sum += num ** 3
        
    # Return the sum of the cubes and squares
    return cube_sum + square_sum