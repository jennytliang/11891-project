def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: sum
	'''

    return sum([(abs(i)**2) if i%2!=0 else 0 for i in lst])


def double_the_difference(lst):
    return sum(map(lambda x: (x**2) if x%2 != 0 else 0, lst))


def double_the_difference(lst):
    return sum(map(lambda x: x**2 if x%2 != 0 else 0, lst))


def double_the_difference(lst):
    return sum(map(lambda x: x**2 if x%2 else 0, lst))


def double_the_difference(lst):
    return sum(map(lambda x: x**2 if x%2 != 0 else 0, lst))


double_the_difference([1, 3, 2, 0])
double_the_difference([-1, -2, 0])
double_the_difference([9, -2])
double_the_difference([0])

double_the_difference([1, 3, 2, 0])
double_the_difference([-1, -2, 0])
double_the_difference([9, -2])
double_the_difference([0])

double_the_difference([1, 3, 2, 0])
double_the_difference([-1, -2, 0])
double_the_difference([9, -2])
double_the_difference([0])

double_the_difference([1, 3, 2, 0])
double_the_difference([-1, -2, 0])
double_the_difference([9, -2])
double_the_difference([0])
