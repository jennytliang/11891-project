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
	Do not include these tokens in the code: # Your code here #
	'''
    # Your code here
    ans = 0
    for el in lst:
        if type(el) != int:
            continue
        if el % 2 == 1:
            ans += el ** 2
    return ans


def double_the_difference2(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code: ans =
	Do not include these tokens in the code: # Your code here #
	'''
    # Your code here
    return sum(map(lambda x: x ** 2 if x % 2 == 1 else 0, filter(lambda x: type(x) == int, lst)))


print(double_the_difference([1, 3, 2, 0]))
print(double_the_difference([-1, -2, 0]))
print(double_the_difference([9, -2]))
print(double_the_difference([0]))
print(double_the_difference([]))
print(double_the_difference2([1, 3, 2, 0]))
print(double_the_difference2([-1, -2, 0]))
print(double_the_difference2([9, -2]))
print(double_the_difference2([0]))
print(double_the_difference2([]))
