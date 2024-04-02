def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8

print(is_equal_to_sum_even(5))
assert(is_equal_to_sum_even(8) == True)
assert(is_equal_to_sum_even(7) == False)
assert(is_equal_to_sum_even(17) == True)
assert(is_equal_to_sum_even(11) == False)
assert(is_equal_to_sum_even(14) == True)
assert(is_equal_to_sum_even(4) == True)
assert(is_equal_to_sum_even(3) == False)