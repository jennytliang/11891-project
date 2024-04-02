def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def is_prime(n: int):
    """Returns True if n is a prime number
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(2019)
    False
    """
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def prime_numbers(n: int):
    """Returns a list of prime numbers from 2 to n
    >>> prime_numbers(10)
    [2, 3, 5, 7]
    >>> prime_numbers(3)
    [2, 3]
    >>> prime_numbers(13)
    [2, 3, 5, 7, 11, 13]
    """
    primes = []
    for x in range(2, n + 1):
        if is_prime(x):
            primes.append(x)
    return primes


def sum_primes(n: int):
    """Returns the sum of prime numbers from 2 to n
    >>> sum_primes(10)
    17
    >>> sum_primes(3)
    5
    >>> sum_primes(13)
    37
    """
    return sum(prime_numbers(n))


def all_same(l: list):
    """Returns True if all the elements of the list l are the same
    >>> all_same([1, 1, 1, 1])
    True
    >>> all_same([1, 2, 1, 1])
    False
    >>> all_same([1])
    True
    """
    return len(set(