def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    if a <= 0:
        return False

    for i in range(2, a):
        if a % i == 0:
            if is_prime(i):
                a = a // i
                if is_prime(a):
                    return True
                else:
                    return False
            else:
                return False


def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def test_is_multiply_prime():
    assert is_multiply_prime(30) is True
    assert is_multiply_prime(225) is True
    assert is_multiply_prime(10) is False
    assert is_multiply_prime(5) is False
    assert is_multiply_prime(11) is False
    assert is_multiply_prime(25) is False
    assert is_multiply_prime(12) is False
    assert is_multiply_prime(13) is False
    assert is_multiply_prime(15) is False
    assert is_multiply_prime(26) is False
    assert is_multiply_prime(29) is False
    assert is_multiply_prime(31) is True
    assert is_multiply_prime(32) is False
    assert is_multiply_prime(33) is True
    assert is_multiply_prime(34) is False
    assert is_multiply_prime(35) is False
    assert is_multiply_prime(36) is False
    assert is_multiply_prime(37) is True
    assert is_multiply_prime(38) is False
    assert is_multiply_prime(39) is True
    assert is_multiply_prime(40) is False
    assert is_multiply_prime(41) is True
    assert is_multiply_prime(42) is False
    assert is_multiply_prime(43) is True
    assert is_multiply_prime(4