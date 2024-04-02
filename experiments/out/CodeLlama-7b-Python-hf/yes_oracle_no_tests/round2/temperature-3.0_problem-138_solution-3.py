def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: 8 and
	Do not include these tokens in the code: 0 def is _ equal _ to
	"""

    return 8 % n == 0


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(9) == True
    is_equal_to_sum_odd(10) == False
    is_equal_to_sum_odd(12) == False
    
	Include these tokens in the code: 9 and
	Do not include these tokens in the code: 0 def is _ equal _ to
	"""

    return 9 % n == 0


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and exactly 2 positive odd numbers
    Example
    is_equal_to_sum_even_odd(10) == True
    is_equal_to_sum_even_odd(12) == True
    is_equal_to_sum_even_odd(14) == False
    
	Include these tokens in the code: 10 and
	Do not include these tokens in the code: 0 def is _ equal _ to
	"""

    return 10 % n == 0


def is_equal_to_sum_even_odd_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number, 2 positive odd numbers and exactly 1 positive even number
    Example
    is_equal_to_sum_even_odd_even(14) == True
    is_equal_to_sum_even_odd_even(16) == True
    is_equal_to_sum_even_odd_even(18) == False
    
	Include these tokens in the code: 14 and
	Do not include these tokens in the code: 0 def is _ equal _ to
	"""

    return 14 % n == 0


def is_equal_to_sum_even_odd_odd(n):
