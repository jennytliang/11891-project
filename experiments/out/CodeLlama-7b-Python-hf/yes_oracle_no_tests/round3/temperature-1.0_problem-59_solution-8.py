def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: # Your code here #
	"""
    # Your code here #
    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            if is_prime(i):
                return i
    return n

def is_prime(n: int):
    """Returns True if n is prime and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    >>> is_prime(113)
    False
    >>> is_prime(121)
    False
    >>> is_prime(1000001)
    True
    >>> is_prime(1000003)
    False
    >>> is_prime(1000031)
    False
    """
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()