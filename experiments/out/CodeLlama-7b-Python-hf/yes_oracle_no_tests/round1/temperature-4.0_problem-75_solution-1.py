def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    prime_list = [2,3,5,7]
    for prime in prime_list:
        if a % prime == 0:
            a = a / prime
            if a < 100:
                return True
            else:
                return False
        else:
            return False


def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(12) == False
    assert is_multiply_prime(25) == False
    assert is_multiply_prime(24) == False
    assert is_multiply_prime(99) == False
    assert is_multiply_prime(60) == True
    assert is_multiply_prime(75) == True
    assert is_multiply_prime(90) == True
    assert is_multiply_prime(100) == False
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(15) == False
    assert is_multiply_prime(36) == False
    assert is_multiply_prime(19) == False
    assert is_multiply_prime(69) == False
    assert is_multiply_prime(101) == False
    assert is_multiply_prime(22) == False
    assert is_multiply_prime(28) == False
    assert is_multiply_prime(32) == False
    assert is_multiply_prime(35) == False
    assert is_multiply_prime(37) == False
    assert is_multiply_prime(39) == False
    assert is_multiply_prime(42) == False
    assert is_multiply_prime(45) == False
    assert is_multiply_prime(48) == False
    assert is_multiply_prime(51) == False
    assert is_multiply_prime(54) == False
    assert is_multiply_prime(57) == False
    assert is_multiply_prime(