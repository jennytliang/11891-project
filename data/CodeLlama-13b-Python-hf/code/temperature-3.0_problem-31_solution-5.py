def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def goldbach(n):
    """Return a list of the sum of two primes for which the sum is equal to n.
    >>> goldbach(10)
    (3, 7)
    >>> goldbach(9)
    (3, 6)
    >>> goldbach(15)
    (5, 10)
    """
    "*** YOUR CODE HERE"