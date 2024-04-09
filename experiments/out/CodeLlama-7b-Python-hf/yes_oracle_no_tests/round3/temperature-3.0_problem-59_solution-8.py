def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # for i in range(2, n // 2 + 1):
    #     if n % i == 0:
    #         n //= i
    #         is_prime.append(False)
    # return n
    largest_prime = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime


def is_prime(n: int):
    """Return True if n is a prime number.
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    >>> is_prime(77)
    True
    >>> is_prime(961)
    True
    >>> is_prime(870)
    False
    >>> is_prime(960)
    False
    >>> is_prime(1000)
    False
    >>> is_prime(1024)
    False
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert not is_prime(12)
    assert not is_prime(15)
    assert not is_prime(23)
    assert not is_prime(25)


def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(1000000007) == 7
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(100) == 5
    assert largest_prime_factor(17) == 17
   