def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    # Your code here
    # print(n)
    # print(is_prime(n))
    # print(largest_prime_factor(n))
    # print(largest_prime_factor(13195))
    # print(largest_prime_factor(2048))
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


def is_prime(n):
    """Returns True if n is prime.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
