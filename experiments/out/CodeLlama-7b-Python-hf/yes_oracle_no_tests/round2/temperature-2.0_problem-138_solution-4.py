def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _ sum
	"""

    return n % 2 == 0 and n == (2**4)


print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == False
    is_equal_to_sum_odd(8) == True
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _ sum
	"""

    return n % 2 == 1 and n == (3**3)


print(is_equal_to_sum_odd(4))
print(is_equal_to_sum_odd(6))
print(is_equal_to_sum_odd(8))


def is_equal_to_sum_even_or_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    and 4 positive even numbers
    Example
    is_equal_to_sum_even_or_odd(4) == True
    is_equal_to_sum_even_or_odd(6) == False
    is_equal_to_sum_even_or_odd(8) == True
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _ sum
	"""

    return n % 2 == 0 and n == (3**3) + (2**4) or n % 2 == 1 and n == (3**3) + (2**4)


print(is_equal_to_sum_even_or_odd(4))
print(is_equal_to_sum_even_or_odd(6))
print(is_equal_to_sum