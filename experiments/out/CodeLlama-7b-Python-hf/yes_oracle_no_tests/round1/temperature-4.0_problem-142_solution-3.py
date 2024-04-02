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
    # add your code here
    ans = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            ans += lst[i]**2
        elif i % 4 == 0:
            ans += lst[i]**3
        else:
            ans += lst[i]
    return ans

def test_function(test_case):
    answer = sum_squares(test_case[0])
    if answer == test_case[1]:
        print("Pass!")
    else:
        print("Fail!")

test_function([[1,2,3],6])
test_function([[1,2,3,4,5],140])
test_function([[1,2,3,4,5,6],1224])
test_function([[1,2,3,4,5,6,7],1000])
test_function([[1,2,3,4,5,6,7,8],10000])
test_function([[1,2,3,4,5,6,7,8,9],100000])
test_function([[1,2,3,4,5,6,7,8,9,10],1000000])
test_function([[1,2,3,4,5,6,7,8,9,10,11],10000000])
test_function([[1,2,3,4,5,6,7,8,9,10,11,12],100000000])
test_function([[1,2,3,4,5,6,7,8,9,10,11,12,13],1000000000])
test_function([[1,2,3,4,5,6,7,8,9,10,11,12,13,14],10000000000])
test_function([[1