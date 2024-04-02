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
    even_total = 0
    odd_total = 0
    
    for num in lst:
        if num % 2 == 0:
            even_total += num
        elif num > 0:
            odd_total += pow(num, 2)
            
    return pow(odd_total, 2)


double_the_difference([1, 3, 2, 0]) # → 10
double_the_difference([-1, -2, 0]) # → 0
double_the_difference([9, -2]) # → 81
double_the_difference([0])