def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: for i in range ( 2 , n ):
	"""
    largest_divisor = 0
    for i in range(2, n):
        if n % i == 0:
            largest_divisor = i
    return largest_divisor


def sum_divisors(n: int) -> int:
    """ Return the sum of all divisors of n, not including n 
    >>> sum_divisors(10)
    21
    """
    divisors = set()
    for i in range(1, n):
        if n % i == 0:
            divisors.add(i)
    return sum(divisors)


def is_prime(n: int) -> bool:
    """ Return True if n is a prime number, False otherwise
    >>> is_prime(10)
    False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_divisors(n: int) -> list:
    """ Return a list of all prime divisors of n 
    >>> prime_divisors(15)
    [3, 5]
    """
    divisors = set()
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i):
                divisors.add(i)
    return list(divisors)


def sum_proper_divisors(n: int) -> int:
    """ Return the sum of all proper divisors of n (divisors should not include n)
    >>> sum_proper_divisors(15)
    10
    """
    divisors = set()
    for i in range(1, n):
        if n % i == 0:
            divisors.add(i)
    return sum(divisors)


def is_perfect(n: int) -> bool:
    """ Return True if n is a perfect number, False otherwise
    >>> is_perfect(6)
    True
    """
    return sum_proper_divisors(n) ==