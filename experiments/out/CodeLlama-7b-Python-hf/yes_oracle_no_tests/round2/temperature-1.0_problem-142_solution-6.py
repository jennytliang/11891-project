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
    # code goes here
    # Your code must be like this
    # ans: int = 0
    # n: int = len(lst)
    # for idx in range(n):
    #     ans += 1

    # return ans

    # An alternate version
    # 1 3 6 10 15 21 28 36 ....
    # 2 4 8 12 16 24 32 40 ....
    # If index is multiple of 4 then cube else square
    ans = 0
    for item in lst:
        # if not(idx % 3) or not(idx % 4):
        if not(lst.index(item) % 4):
            ans += (item ** 3)
        else:
            ans += item ** 2
    return ans


x = [1, 2, 3, 4]
y = []
z = [-1, -5, 2, -1, -5]
print(sum_squares(x))
print(sum_squares(y))
print(sum_squares(z))
