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

    # Add a line of code here
    if lst == []:
        ans = 0
    else:
        for k in range(len(lst)):
            if k%3==0:
                lst[k] = lst[k] * lst[k]
            if k%4==0 and (k%3!=0):
                lst[k] = lst[k] * lst[k] * lst[k]
        ans = sum(lst)

    return ans
            #end