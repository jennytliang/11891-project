def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8


def is_equal_to_sum_n(n, m):
    """Evaluate whether the given number n can be written as the sum of exactly m positive numbers
    Example
    is_equal_to_sum_n(4, 2) == False
    is_equal_to_sum_n(6, 2) == False
    is_equal_to_sum_n(8, 2) == True
    is_equal_to_sum_n(8, 3) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= m * (m - 1) // 2


def is_equal_to_sum_n_with_condition(n, m, condition):
    """Evaluate whether the given number n can be written as the sum of exactly m positive numbers
    Example
    is_equal_to_sum_n_with_condition(4, 2, lambda x: x % 2 == 0) == False
    is_equal_to_sum_n_with_condition(6, 2, lambda x: x % 2 == 0) == False
    is_equal_to_sum_n_with_condition(8, 2, lambda x: x % 2 == 0) == True
    is_equal_to_sum_n_with_condition(8, 3, lambda x: x % 2 == 0) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= m * (m - 1) // 2
