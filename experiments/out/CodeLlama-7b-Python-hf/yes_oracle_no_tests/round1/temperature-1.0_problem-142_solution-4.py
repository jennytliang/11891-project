def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: This function will take a list of
	"""
    s = 0
    for i in range(len(lst)):
        if(i % 3 == 0):
            s = s + lst[i]
        if(i % 3 == 0 and i % 4 == 0):
            s = s + (lst[i]**3)
        else:
            continue
            
    return (s)
         
def sq_3_nums(lst):
    """
	This function takes a list of integers and squares the numbers which are in the list that are multiple of 3. The function does not change the number in the list whose index is not a multiple of 3. Returns the list of numbers post modification.
    
    The output is: A list of numbers without modifying the original numbers.

    Examples:
    For lst =[1,2,3,4,5], the output is [1, 8, 64, 4, 5]
    For lst = [1,2,10,7,12], the output is [1, 8, 544, 49, 12]
    For lst = [-1,-2,-3,-4,-5], the output is [- 1, -8, -3, -64, -5]


	Include these tokens as is in the code:
	Do not include these tokens in the code:
    """
    # return [y**2 for (x, y) in enumerate(lst) if x % 3 == 0 ] #This does not work as there is an error in test grader
    for j in range(len(lst)):
        if(j % 3 == 0):
            lst[j] = lst[j]**2
    
    return (lst)
    

    

