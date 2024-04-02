def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""
    if n % 2 == 0:
        return 2
    else:
        for i in range(3, n):
            if n % i == 0:
                if is_prime(i):
                    return i


def is_prime(n: int):
    """Returns True if n is prime and False otherwise.
    >>> is_prime(3)
    True
    >>> is_prime(11)
    True
    >>> is_prime(71)
    False
    >>> is_prime(73)
    True
    >>> is_prime(75)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n: int):
    """Return the sum of the digits of n.
    >>> sum_of_digits(10) # 1 + 0 = 1
    1
    >>> sum_of_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_of_digits(12345)
    15
    >>> a = sum_of_digits(12345)
    >>> a # check that this was not modified
    15
    """
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


def count_digits(n: int):
    """Return the count of the digits of n.
    >>> count_digits(10) # 1 has one digit
    1
    >>> count_digits(4224) # 4, 2, 2, and 4 are each one digit
    4
    >>> count_digits(3840) # 3, 8, 4, and 0 are each one digit
    4
    """
    if n == 0:
        return 0
    return 1 + count