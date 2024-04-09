def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 100:
        for i in range(2,a):
            if a % i == 0:
                for j in range(2,i):
                    if i % j == 0:
                        for k in range(2,j):
                            if j % k == 0:
                                return True
        return False
        

def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(25) == False
    assert is_multiply_prime(100) == False
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(4) == False
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(6) == False
    assert is_multiply_prime(7) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(9) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(11) == False
    assert is_multiply_prime(12) == False
    assert is_multiply_prime(13) == False
    assert is_multiply_prime(14) == False
    assert is_multiply_prime(15) == False
    assert is_multiply_prime(16) == False
    assert is_multiply_prime(17) == False
    assert is_multiply_prime(18) == False
    assert is_multiply_prime(19) == False
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(21) == False
    assert is_multiply_prime(22) == False
    assert is_multiply_prime(23) == False
    assert is_multiply_prime(24) == False
    assert is_