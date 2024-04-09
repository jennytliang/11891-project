def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # write code here
    return True


# TESTS
assert is_multiply_prime(30)
assert not is_multiply_prime(20)
assert not is_multiply_prime(100)
assert not is_multiply_prime(9)
assert not is_multiply_prime(12)
assert not is_multiply_prime(25)
assert not is_multiply_prime(10)
assert not is_multiply_prime(22)
