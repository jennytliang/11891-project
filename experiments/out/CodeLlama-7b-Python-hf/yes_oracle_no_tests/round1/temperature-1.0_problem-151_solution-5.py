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
	Do not include these tokens in the code: sum
	'''
    
    #YOUR CODE HERE
  l=[]
  n=0
  for i in lst: #This goes through each value in the list lst and assigns them to i
      if i %2 != 0 and i >= 0 and i % 1 == 0: #This checks if i is not divisible by 2 and that i can be divided by 1
        n=l[n]**2 #n keeps track of squared values that are odd
		l.append(n) #Then we append n to l
  return sum(l) #Then return the sum of l
  

print(double_the_difference([1, 3, 2, 0]))