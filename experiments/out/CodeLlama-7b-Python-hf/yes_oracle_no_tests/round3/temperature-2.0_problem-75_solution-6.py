def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	Do not include these tokens in the code: #
	"""
    # BEGIN CODE
    if a <= 100:
        if a == 2:
            return True
        elif a % 2 == 0:
            return False
        else:
            primes = [3, 5, 7]
            for prime in primes:
                if a % prime == 0:
                    return True
        return False
    else:
        return False
    # END CODE


def test_is_multiply_prime():
    assert is_multiply_prime(30)
    assert not is_multiply_prime(25)
    assert not is_multiply_prime(12)
    assert not is_multiply_prime(60)
    assert not is_multiply_prime(101)
    assert not is_multiply_prime(15)
    assert not is_multiply_prime(70)
    assert not is_multiply_prime(10)
    assert is_multiply_prime(150)
    assert is_multiply_prime(24)


if __name__ == '__main__':
    test_is_multiply_prime()
