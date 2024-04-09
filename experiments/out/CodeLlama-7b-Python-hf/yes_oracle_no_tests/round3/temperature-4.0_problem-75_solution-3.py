def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    pass


def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(29) == False
    assert is_multiply_prime(120) == True
    assert is_multiply_prime(90) == False
    assert is_multiply_prime(15) == False
    assert is_multiply_prime(36) == True
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(121) == False
    assert is_multiply_prime(100) == False
    assert is_multiply_prime(101) == False
    assert is_multiply_prime(123456) == False
