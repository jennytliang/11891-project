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
    sum = 0
    for i in range(len(lst)):
        if i%3==0:
            sum += lst[i]**2
        elif i%4==0:
            sum += lst[i]**3
        else:
            sum += lst[i]
    return sum



print(sum_squares([1,2,3]))
print(sum_squares([1,2,3,4]))
print(sum_squares([1,2,3,4,5,6]))
print(sum_squares([]))
print(sum_squares([1,2,3,4,5,6,7]))
print(sum_squares([-1,-5,2,-1,-5]))
print(sum_squares([-1,-5,2,-1,-5,6]))
