def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: pass def is _
	"""
    pass



def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(26) == False
    assert is_multiply_prime(15) == True
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(9) == False
    assert is_multiply_prime(25) == False
    assert is_multiply_prime(24) == False
    assert is_multiply_prime(18) == False
    assert is_multiply_prime(17) == False
    assert is_multiply_prime(19) == False
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(16) == False
    assert is_multiply_prime(12) == False
    assert is_multiply_prime(13) == False
    assert is_multiply_prime(14) == False
    assert is_multiply_prime(11) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(0) == False
    assert is_multiply_prime(-1) == False
    assert is_multiply_prime(-10) == False
    assert is_multiply_prime(-20) == False
    assert is_multiply_prime(-25) == False
    assert is_multiply_prime(-26) == False
    assert is_multiply_prime(-28) == False
    assert is_multiply_prime(-30) == False
    assert is_multiply_prime(-31) == False
    assert is_multiply_prime(-32) == False
    assert is_multiply_prime(-33) == False
    assert is_multiply_prime(-34) == False
    assert is_multiply_prime(-35) == False
    assert is_multiply_prime(-36) == False
    assert is_multiply_prime