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
    
	Do not include these tokens in the code: elif
	"""



    if n <= 1:
        
        return False
    
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True




def prime_factors(n):
    """Return a list of prime factors for a given number.
    >>> prime_factors(10)
    [2, 5]
    >>> prime_factors(11)
    [11]
    >>> prime_factors(101)
    [101]
    >>> prime_factors(1234567)
    [7, 6, 5, 3, 2]
    >>> prime_factors(13441)
    [13, 1]
    >>> prime_factors(105)
    [5, 3, 1]
    >>> prime_factors(27)
    [3, 3]
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(25)
    [5, 5]
    >>> prime_factors(106)
    [2, 3, 7]
    >>> prime_factors(104)
    [2, 2, 2, 7]
    
	Do not include these tokens in the code: elif
    """



    primes = []
    while n > 1:
        for i in range(2, n):
            if n % i == 0:
                primes.append(i)
                n = n // i
                break
    return primes




def prime_sum(n):
    """Return the sum of the first n prime numbers.
    >>> prime_sum(3)
    10
    >>> prime_sum(5)
    20
    >>> prime_sum(7)
    37
    >>> prime_sum(10)
    187
    >>> prime_sum(15)
    883
    >>> prime_sum(20)
    142