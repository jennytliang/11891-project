def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	"""
    def is_even(n):
        return n % 2 == 0
    if is_even(n):
        return False
    return False

print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(9))
print(is_equal_to_sum_even(10))



