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
    result = 0
    for i in lst:
        try:
            if abs(i) != i:
                i = round(i, 1)
            if i % 2 != 0 and i >= 0:
                result += i ** 2
        except Exception:
            pass
    print(result)
    return result

if __name__ == '__main__':
    double_the_difference([1, 3, 9, 2, 13, 34, -8, 4])
    double_the_difference([-1, 10, -30])