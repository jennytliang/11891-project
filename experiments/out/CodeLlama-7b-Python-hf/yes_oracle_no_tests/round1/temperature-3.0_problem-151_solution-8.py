def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code: ans =
	'''
    # your code here
    ans = sum([(i**2) for i in lst if i % 2 == 1])
    return ans


# double_the_difference([1, 3, 2, 0])
# double_the_difference([-1, -2, 0])
# double_the_difference([9, -2])
# double_the_difference([0])
# double_the_difference([])
# double_the_difference([1, 3, 2, 0, 5])
# double_the_difference([1, 3, 2, 0, 5, 7, 8])
# double_the_difference([1, 3, 2, 0, 5, 7, 8, 10])
# double_the_difference([1, 3, 2, 0, 5, 7, 8, 10, 100])
