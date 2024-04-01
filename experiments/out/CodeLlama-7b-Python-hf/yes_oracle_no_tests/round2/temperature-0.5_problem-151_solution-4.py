def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: # code goes here
	'''
    if len(lst) == 0:
        return 0
    else:
        return sum([(abs(i) ** 2) for i in lst if i % 2 == 1])



double_the_difference([1, 3, 2, 0])
double_the_difference([-1, -2, 0])
double_the_difference([9, -2])
double_the_difference([0])
double_the_difference([3, 2, 2, 5])