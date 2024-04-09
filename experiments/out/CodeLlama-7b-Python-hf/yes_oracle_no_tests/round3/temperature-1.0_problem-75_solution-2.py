def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: <
	"""


  


def test_cases():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(225) == True
    assert is_multiply_prime(235) == False
    assert is_multiply_prime(135) == False
    assert is_multiply_prime(36) == True
    assert is_multiply_prime(26) == False
    assert is_multiply_prime(25) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(9) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(7) == False
    assert is_multiply_prime(6) == False
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(4) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(0) == False



if __name__ == '__main__':
    test_cases()


