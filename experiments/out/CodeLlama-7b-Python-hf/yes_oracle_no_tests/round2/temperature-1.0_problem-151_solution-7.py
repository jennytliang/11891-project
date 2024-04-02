def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code: num
	Do not include these tokens in the code: i
	'''

    ans = 0

  #  for num in lst:                                    # Checks for validity of number
  #      if num >= 0 and type(num) == int:
  #          if num % 2 != 0:
  #              ans += num ** 2

  #  return ans


    for num in lst:                                    # Checks for validity of number
        for char in str(num):
            if char in '-+' or '.' in str(num):
                break
            if num != -1 and num != 0 and type(num) != int:
                print('Input is invalid')
            elif num == -1 or num == 0:
                ans += 0
            elif num % 2 != 0:
                ans += num ** 2
    return ans

test_list = [1, 3, 2, 0, 5]
print(f'double_the_difference({test_list}) returns {double_the_difference(test_list)}')





