def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Do not include these tokens in the code: # your code here
	'''
    # for loop
    # sum = 0
    # for num in lst:
    #     if num in range(1,5):
    #         sum += num**2
    #     else:
    #         pass
    # return sum

    # list comprehension
    # return sum([num**2 for num in lst if num in range(1,5)])

    # one line lambda
    return sum([num**2 for num in lst if num in range(1,5)])