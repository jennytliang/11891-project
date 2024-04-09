def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str , range
	"""
    return " ".join(map(str, range(n+1)))


def is_prime(n: int) -> bool:
    """ Return True if n is a prime number.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    
	Include these tokens in the code: range
	
	"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def list_of_primes(n: int) -> list:
    """ Return a list of prime numbers up to and including n.
    >>> list_of_primes(10)
    [2, 3, 5, 7]
    >>> list_of_primes(80)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
    """
    return [i for i in range(n+1) if is_prime(i)]


def count_primes(n: int) -> int:
    """ Return the number of prime numbers up to and including n.
    >>> count_primes(10)
    4
    >>> count_primes(80)
    12
    """
    return len(list_of_primes(n))


def gcd(a: int, b: int) -> int:
    """ Return the greatest common divisor of a and b.
    >>> gcd(7, 3)
    1
    >>> gcd(18, 12)
    6
    >>> gcd(13, 103)
    1
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def l