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
    
    numbers = lst
    
    for i in range(len(numbers)):
        
        if numbers[i] % 2 != 0:
            
            numbers[i] = numbers[i] ** 2
        
        else:
            
            numbers[i] == 0
    
    # add all elements of array
    total = sum(numbers)
    
    return total
        
    
    
answer = double_the_difference([1, 3, 2, 0])
#print (answer)
    


answer = double_the_difference([-30, -1, 0, 0, 10])
#print (answer)
    


answer = double_the_difference([0, -4, 2, 9, 0])
#print (answer)