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
    # 23 lines of code is expected (incredibly hard, but doable)
    return sum([x**3 if i%3==0 else x**2 if i%4==0 else x for i,x in enumerate(lst)])

def sum_squares_2(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its 
    index is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function 
    will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all 
    entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: This function will take a list of
    """
    # 22 lines of code is expected (easy, but tough)
    lst = sorted(range(len(lst)), key=lambda i: lst[i]%4!=0 or i%3!=0)
    return sum([lst[i] for i in lst])
    
def sum_squares_3(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index 
    is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1