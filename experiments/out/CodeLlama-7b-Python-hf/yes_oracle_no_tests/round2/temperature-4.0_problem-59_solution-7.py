def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            n = n // i
            if n == 1:
                return i
        i += 1
    return n


def sum_of_digits(n):
    """Sum all the digits of n.

    >>> sum_of_digits(10) # 1 + 0 = 1
    1
    >>> sum_of_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_of_digits(1234567890)
    45
    >>> a = sum_of_digits(123) # 123
    >>> a # 123 should not change!
    123
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


def count_digits(n):
    """Count the number of digits in n.

    >>> count_digits(123)
    3
    >>> count_digits(4567890)
    7
    >>> a = count_digits(9) # 9
    >>> a # 9 should not change!
    9
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n:
        count += 1
        n //= 10
    return count


def is_prime(n):
    """Returns True if n is a prime number, otherwise False.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    >>> is_prime(2048)
    False
    >>> is_prime(347)
    True
    """
    "*** YOUR CODE HERE ***