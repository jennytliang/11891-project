def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    def is_prime(p):
        if p == 2:
            return True
        if p <= 1 or p % 2 == 0:
            return False
        for i in range(3, int(p ** 0.5) + 1, 2):
            if p % i == 0:
                return False
        return True

    largest_prime = 1
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i):
                largest_prime = i
    return largest_prime


print(largest_prime_factor(13195))
print(largest_prime_factor(2048))
