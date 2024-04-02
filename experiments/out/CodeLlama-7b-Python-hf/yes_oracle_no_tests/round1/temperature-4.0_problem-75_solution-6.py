def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""

    def is_prime(number):
        """
        Check if the number is prime.
        """
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    if a <= 100:
        if is_prime(a):
            return False
        else:
            for i in range(2, a):
                if is_prime(i) and is_prime(a / i):
                    if is_prime(a / i / i):
                        return True
    return False


def test_is_multiply_prime():
    assert is_multiply_prime(30)
    assert not is_multiply_prime(5)
    assert not is_multiply_prime(10)
    assert not is_multiply_prime(50)
    assert not is_multiply_prime(100)
    assert is_multiply_prime(60)
    assert not is_multiply_prime(61)
    assert not is_multiply_prime(1000)
