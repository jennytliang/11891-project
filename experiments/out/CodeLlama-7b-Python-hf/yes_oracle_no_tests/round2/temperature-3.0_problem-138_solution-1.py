def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	"""

    return n >= 8 and n % 2  == 0 and n == (n//2)**2


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == True
    is_equal_to_sum_odd(8) == False
    
	"""

    return n >= 6 and n % 2 != 0 and n == (n//2)**2 + 1


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(6) == False
    is_equal_to_sum_even_and_odd(8) == True
    is_equal_to_sum_even_and_odd(10) == True
    
	"""

    return n >= 10 and n % 2 == 0 and n == (n//2)**2 + 1


def is_equal_to_sum_even_and_odd_and_one(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number and 1 positive odd number and 1 positive odd number
    Example
    is_equal_to_sum_even_and_odd_and_one(4) == False
    is_equal_to_sum_even_and_odd_and_one(6) == False
    is_equal_to_sum_even_and_odd_and_one(8) == False
    is_equal_to_sum_even_and_odd_and_one(10) == True
    is_equal_to_sum_even_and_odd_and_one(12) == True
    
	"""