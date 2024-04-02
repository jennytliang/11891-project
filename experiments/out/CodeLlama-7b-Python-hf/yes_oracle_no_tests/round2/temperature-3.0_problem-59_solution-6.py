def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: # = [ True ] *
	"""
    "*** YOUR CODE HERE ***"
    if n <= 1:
        return 1
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            j = 2
            while i * j <= n:
                if i * j == n:
                    return i
                j += 1
    return 1


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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n % 10 == 0:
            return n // 10
        else:
            return n % 10 + sum_of_digits(n // 10)


def is_prime(n: int):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> g