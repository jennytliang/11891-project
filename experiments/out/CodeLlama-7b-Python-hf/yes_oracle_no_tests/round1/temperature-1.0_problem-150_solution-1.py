def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n > 1 :
	"""
    if is_prime(n):
        return x
    return y

def is_prime(n):
    """
    Returns True if n is a prime number
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(20) == False
    assert is_prime(21) == True
    assert is_prime(22) == False
    assert is_prime(23) == True
    assert is_prime(24) == False
    assert is_prime(25) == False
    assert is_prime(26) == False
    assert is_prime(27) == True
    assert is_prime(28) == False
    assert is_prime(29) == True
    assert is_prime(30) == False
    assert is_prime(31) == True
    assert is_prime(32) == False
    assert is_prime(33) == True
    assert is_prime(34) == False
    assert is_prime(35