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
    
	Include these tokens in the code: n _ sqrt = 1 while
	"""

    if n <= 1:
         return False
    if n <= 3:
         return True
    if n % 2 == 0 or n % 3 == 0:
         return False
    i = 5
    while i * i <= n:
         if n % i == 0 or n % (i + 2) == 0:
             return False
         i = i + 6
    return True

def prime_factors(n):
    """
    >>> prime_factors(1)
    []
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(7)
    [7]
    >>> prime_factors(15)
    [3, 5]
    >>> prime_factors(4)
    [2, 2]
    >>> prime_factors(3**4 * 5)
    [3, 3, 3, 3, 5]
    >>> prime_factors(1234123412341231)
    [11, 41, 121]
    """
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            n = n // i
            factors.append(i)
        else:
            i = i + 1
    return factors

def prime_factors_mult(n):
    """Return a dictionary of prime factors and powers of n.
    >>> prime_factors_mult(8)
    {2: 3}
    >>> prime_factors_mult(10)
    {5: 1, 2: 1}
    >>> prime_factors_mult(12)
    {2: 2, 3: 1}
    >>> prime_factors_mult(11)
    {11: 1}
    >>> prime_factors_mult(17)
    {17: 1}
    >>> prime_factors_mult(4)
    {2: 2}
    >>> prime_factors_mult(2