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
    for i in lst:
        if i > 0 and i % 2 == 1:
            ans += i ** 2
    return ans

#Tests
def double_the_difference_test():
    input_values = [
        [[1, 3, 2, 0], 10],
        [[-1, -2, 0], 0],
        [[9, -2], 81],
        [[0], 0],
        [[1, 2, 3, 4, 5], 55],
        [[0, 1, 2, 3, 4, 5], 55],
        [[-1, 2, 3, 4, 5], 28],
        [[-1, -2, -3, -4, -5], 0],
        [[1, 3, 5, 7, 9], 55],
        [[], 0]
    ]
    for values in input_values:
        inp, exp = values
        print('running double_the_difference({})'.format(inp))
        ans = double_the_difference(inp)
        if ans == exp:
            print('PASSED')
        else:
            print('FAILED, expected {}, got {}'.format(exp, ans))


if __name__ == '__main__':
    double_the_difference_test()
