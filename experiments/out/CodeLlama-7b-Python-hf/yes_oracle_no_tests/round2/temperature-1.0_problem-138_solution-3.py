def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _
	"""

    return n % 2 == 0 and n == sum([int(n/2), int(n/2), int(n/2), int(n/2)])



print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))































































































































































































































































































































































































































