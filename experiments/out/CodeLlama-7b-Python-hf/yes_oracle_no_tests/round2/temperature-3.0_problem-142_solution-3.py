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
    # Write your code here.
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            sum += lst[i] ** 3
        else:
            sum += lst[i]
    return sum
    


#Below is a function for testing your code
def test_function(test_case):
    answer = sum_squares(test_case)
    if answer == test_case_answers[test_case]:
        print("Pass")
    else:
        print("Fail")

test_case_answers = {
    [1,2,3]: 6,
    []: 0,
    [-1,-5,2,-1,-5]: -126
    }
test_case = [1,2,3]
test_function(test_case)
test_case = []
test_function(test_case)
test_case = [-1,-5,2,-1,-5]
test_function(test_case)
