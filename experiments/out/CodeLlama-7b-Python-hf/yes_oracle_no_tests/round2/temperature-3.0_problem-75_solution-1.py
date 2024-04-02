def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: pass def is _ pal
	"""
    if a < 100:
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        if a in prime_list:
            return True
        else:
            return False
    else:
        return "Out of range"


def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(50) == True
    assert is_multiply_prime(99) == False
    assert is_multiply_prime(100) == "Out of range"
