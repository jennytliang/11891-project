def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Do not include these tokens in the code: # pass
	'''
    # my_list = [int(x) for x in lst if type(int(x)) == int]
    result = 0
    for value in lst:
        try:
            val = int(value)
        except (TypeError, ValueError):
            pass
        else:
            if (val % 2) != 0:
                result += val**2
    return result
