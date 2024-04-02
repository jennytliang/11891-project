def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    # YOUR CODE HERE
    return n >= 8 and n % 2 == 0

# TESTS
assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(10) == False
assert is_equal_to_sum_even(12) == True
assert is_equal_to_sum_even(14) == False
assert is_equal_to_sum_even(16) == True
assert is_equal_to_sum_even(18) == False
assert is_equal_to_sum_even(20) == True

