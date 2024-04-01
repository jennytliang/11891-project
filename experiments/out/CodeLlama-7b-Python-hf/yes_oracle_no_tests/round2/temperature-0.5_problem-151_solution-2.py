def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Do not include these tokens in the code: # assert type ( lst )
	'''
    odds = []
    for i in lst:
        if i >= 0 and int(i) == i:
            if i % 2 == 1:
                odds.append(i * i)
    return sum(odds)


# double_the_difference([3, 0, 3, 2, 0])