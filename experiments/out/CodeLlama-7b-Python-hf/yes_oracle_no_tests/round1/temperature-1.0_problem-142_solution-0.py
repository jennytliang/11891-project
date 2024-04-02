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
	
	output = 0
	for idx, item in enumerate(lst):
		if (idx % 3 == 0):
			# square it item
			output = output + item ** 2
		elif (idx % 4 == 0 and idx % 3 != 0):
			# cube it item
			output = output + item ** 3
		else:
			# add it item
			output = output + item
	return output
	
			
def test_function(test_case):
    output = sum_squares(test_case)
    print (output)
    if output == 6:
        print("Pass")
    else:
        print("Fail")

test_case = [1,2,3]
test_function(test_case)

test_case = []
test_function(test_case)

test_case = [-1,-5,2,-1,-5]
test_function(test_case)