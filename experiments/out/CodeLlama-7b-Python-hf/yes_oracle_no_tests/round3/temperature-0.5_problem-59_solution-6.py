def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: if n < 2 :
	"""
    "*** YOUR CODE HERE ***"
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


def sum_of_digits(n: int):
    """Return the sum of the digits of n.
    >>> sum_of_digits(10) # 1 + 0 = 1
    1
    >>> sum_of_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_of_digits(1234567890)
    45
    >>> a = sum_of_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def print_digits(n: int):
    """Print the digits of n starting with the least significant digit.
    >>> print_digits(123)
    3
    2
    1
    """
    "*** YOUR CODE HERE ***"
    print(n % 10)
    if n >= 10:
        print_digits(n // 10)


def print_digits_reversed(n: int):
    """Print the digits of n starting with the most significant digit.
    >>> print_digits_reversed(123)
    1
    2
    3
    """
    "*** YOUR CODE HERE ***"
    if n >= 10:
        print_digits_reversed(n // 10)
    print(n % 10)


def gcd(a: int, b: int):
    """Return the greatest common divisor of a and b.
    >>> gcd(34, 1