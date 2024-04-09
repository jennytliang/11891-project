def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code: == 1 and num >
	Do not include these tokens in the code: !=
	'''


    ans = 0
  
    for num in lst:
        i = 0
        if num > 0:
            if num % 2 != 0:
                i = num ** 2
                ans += i

    return ans



#print(double_the_difference([1, 3, 2, 0]))
#print(double_the_difference([-1, -2, 0]))
#print(double_the_difference([9, -2]))
#print(double_the_difference([0]))



def test_bench():
    test_data = [
                    [[1, 3, 2, 0], 10],
                    [[-1, -2, 0], 0],
                    [[9, -2], 81],
                    [[0], 0]
                ]

    for td in test_data:
        print(double_the_difference(td[0]) == td[1])


#test_bench()
