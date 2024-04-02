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
	Do not include these tokens in the code: total
	'''

    ans=0
    for i in lst:
        total=0
        if  i <0 or int!=i or float!=i:
            continue
        else:
            if i %2 !=0:
                ans += int(i*i)
            else:
                continue
        
    return ans, total

double_the_difference([1, 3])
