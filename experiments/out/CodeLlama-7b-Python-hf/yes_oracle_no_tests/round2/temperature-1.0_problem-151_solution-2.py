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
    ans = 0
    for num in lst:
        if num != int and -1<= num < 0:
            continue
        if num % 2 == 0:
            num = num**2
            ans = ans + num
        else:
            num = num**2
            ans = ans - num
    return ans

def double_the_difference_better(lst):
    '''
    You can also use one line for the logic
    '''
    
    return sum(x**2 if x%2!=0 else -x**2 for x in lst if x%2!=0 or x>=0)

def double_the_difference_better1(lst):
    return sum([x**2 if x%2 != 0 - x**2 if x%2==0 for x in lst if x%2!=0 or x>=0 ])

answer=double_the_difference([1, 3, 2, 0])
print(answer)
print(double_the_difference_better([1, 3, 2, 0]))