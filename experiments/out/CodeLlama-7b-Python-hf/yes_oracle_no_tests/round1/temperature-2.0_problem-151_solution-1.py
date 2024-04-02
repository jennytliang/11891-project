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
	Do not include these tokens in the code: if len ( lst )
	'''
    # your code here
    ans = 0
    for num in lst:
        if num % 2 != 0:
            ans += num*num
    return ans


# 🚨 Don't change any of the code below 
print("expected result:", 10)
print(double_the_difference([1, 3, 2, 0]))

print("expected result:", 0)
print(double_the_difference([-1, -2, 0]))

print("expected result:", 81)
print(double_the_difference([9, -2]))

print("expected result:", 0)
print(double_the_difference([0]))

print("expected result:", 0)
print(double_the_difference([]))










































































