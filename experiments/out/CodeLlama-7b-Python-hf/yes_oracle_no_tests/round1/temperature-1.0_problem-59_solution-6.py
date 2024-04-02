def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    if n <= 2:
        largest_prime_factor = n
    while n % 2 == 0:
        largest_prime_factor = 2
        n /= 2
    up_to = int(n ** 0.5)
    for f in range(3, up_to + 1, 2):
        while n % f == 0:
            largest_prime_factor = f
            n /= f
            break
    while n > 1:
        if is_prime(int(n)):
            largest_prime_factor = n
            break
        up_to = int(n ** 0.5)
        for f in range(up_to, 0, -2):
            while n % f == 0:
                largest_prime_factor = f
                n /= f
                break
        largest_prime_factor += 1
    return int(largest_prime_factor)


def is_prime(n: int):
    """Returns True if n is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(25)
    False
    """
    "*** YOUR CODE HERE ***"
    if n <= 2:
        return n == 2 or n == 1
    if n % 2 == 0:
        return False
    # Checks if its divisble by odd numbers up to its square root

    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()