def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: n
	Do not include these tokens in the code: ( - 8 )
	"""


    
    return n % 2 == 0 and n / 2 == int(n / 2)


# TESTS
assert is_equal_to_sum_even(8)
assert not is_equal_to_sum_even(6)
assert not is_equal_to_sum_even(4)
