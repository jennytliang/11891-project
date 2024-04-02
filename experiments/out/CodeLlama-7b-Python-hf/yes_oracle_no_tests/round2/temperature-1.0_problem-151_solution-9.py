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
	Do not include these tokens in the code: result
	'''
    
    ans = 0
    for x in lst:
        if x >= 0 and x % 2 == 1:
            ans += x**2
    return ans


# A better solution

def double_the_difference(lst):
    return sum([num**2 if num % 2 == 1 else 0 for num in lst])

# Double The Difference - Examples
print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))
print(double_the_difference([]))