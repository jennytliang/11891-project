def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    # Your code here
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

    for i in range(2, n + 1):
        if n % i == 0:
            if is_prime(i):
                return i


print(largest_prime_factor(13195))
print(largest_prime_factor(2048))


def largest_prime_factor(n: int):
    """Return the largest prime factor of n.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    >>> largest_prime_factor(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000L)
    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999