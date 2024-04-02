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
    
	Include these tokens in the code: if n <=
	"""
    # BEGIN PROBLEM 5
    for i in range(2, n-1):
        if n % i == 0:
            return False

    return n > 1
    # END PROBLEM 5
# TEST (cite test_functions) 20 points


def increment(n):
    """Return the sum of the numbers in the range (2, n).
    >>> increment(7) # 2 + 3 + 4 + 5 + 6 + 7 = 28
    28
    >>> increment(8) # 2 + 3 + 4 + 5 + 6 + 7 + 8
    35
    >>> increment(200)
    10100
    """
    # BEGIN PROBLEM 6

    sum = 0     
    for i in range(2, n + 1):
        sum = sum + i

    return sum
    # END PROBLEM 6


def digits(n):
    """Return the digits of n as a string.

    >>> digits(42)
    '42'
    >>> digits(14)
    '14'
    >>> digits(1)
    '1'
    >>> digits(420)
    '420'
    >>> digits(0)
    '0'
    >>> digits(-14) # If you pass in -14, you get an error!
    Traceback (most recent call last):
    ...
    ValueError: n must be non-negative
    """
    if n < 0:
        raise ValueError('n must be non-negative')

    return str(n)


def is_palindrome(n):
    """Returns True if the digits of n is equal to the number reversed
    >>> is_palindrome(12) # False
    False
    >>> is_palindrome(121) # True
    True
    >>> is_palindrome(221) # False
    False
    >>> is_palindrome(222) # True
    True
   