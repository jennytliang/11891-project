def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: # Write your code here
	"""
	# Write your code here
	
	sum_of_even_nums = 0
	
	for i in range(1, n + 1):
		if i % 2 == 0:
			sum_of_even_nums += i
			
	if sum_of_even_nums == n:
		return True
	else:
		return False
		
		
print(is_equal_to_sum_even(8))
