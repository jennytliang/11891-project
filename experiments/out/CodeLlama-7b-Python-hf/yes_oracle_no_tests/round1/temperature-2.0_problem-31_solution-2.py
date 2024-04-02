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
    sqrt = 1
    while sqrt <= n:
        if n % sqrt == 0:
            return False
        sqrt += 2
    return True

def prime_factors(n):
    """Print all the prime factors of a given number.
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(20)
    2
    5
    >>> prime_factors(32)
    2
    2
    2
    >>> prime_factors(25)
    5
    """

    i = 2
    while i <= n:
        if n % i == 0:
            if is_prime(i):
                print(i)
            prime_factors(n // i)
            break
        i += 1

def prime_factors_mult(n):
    """Return a tuple of all the prime factors of a given number.
    >>> prime_factors_mult(36)
    2
    2
    3
    >>> prime_factors_mult(11)
    11
    >>> prime_factors_mult(13)
    13
    >>> prime_factors_mult(20)
    2
    5
    >>> prime_factors_mult(25)
    5
    """

    factors_list = []
    i = 2
    while i <= n:
        if n % i == 0:
            if is_prime(i):
                factors_list.append(i)
            n /= i
        else:
            i += 1
    return factors_list

def prime_factors_dict(n):
    """Return a dictionary of the prime factors and powers of a given number.
    >>> prime_factors_dict(36)
    {2: 2, 3: 1}
    >>> prime_factors_dict(11)
    {11: 1}
    >>> prime_factors_dict(13)
    {13: 1}
    >>> prime_factors_dict(