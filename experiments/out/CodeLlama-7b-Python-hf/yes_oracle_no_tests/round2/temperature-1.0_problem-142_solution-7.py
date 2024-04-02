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
    sum_square = 0
    for idx, i in enumerate(lst): # iterate through the list, access index and element with in operator
        if idx%3 == 0 and idx%4 != 0: # if the index is a multiple of 3 and not of 4 (also cancels out if idx%3 != 0)
            sum_square += i**2 # sum up each element multiplied by itself, e.g. (0**2 + 1**2 + 3**2)
        elif idx%4 == 0: # if the index is a multiple of 4
            sum_square += i**3 # sum up each element multiplied by itself, e.g. (0**3 + 1**3 + 3**3)
    return sum_square # return sum of squares/cubes for each element that satisfies the conditions
            
def test_function(test_case):
    answer = sum_squares(test_case)
    if test_case == []:
        return ("List is empty")
    else:
        return ("Sum of " + str(test_case) + "is " + str(answer))

if __name__ == '__main__':
    test_case_1 = [-1,-5,2,-1,-5]
    test_case_2 = [1,2,3]
    test_case_3 = []
    test_case_4 = [-5,-5,-5,-5]
    print(test_function(test_case_1))
    print(test_function(test_case_2))
    print(test_function(test_case_3))
    print(test_function(test_case_4))