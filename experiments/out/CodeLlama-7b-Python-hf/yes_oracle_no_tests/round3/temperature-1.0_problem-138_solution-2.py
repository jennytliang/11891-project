def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    # return n >= 8 # this is not correct
    # return n >= 4 # this is not correct
    return n >= 4 and n % 2 == 0 # this is correct
    # return n >= 8 and n % 2 == 0 # this is correct

print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(10))
print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))

