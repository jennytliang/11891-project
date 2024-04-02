def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is
	Do not include these tokens in the code: if n <= 2 :
	"""
    "*** YOUR CODE HERE ***"
    largest_prime_factor = 1
    j = 2
    while j <= n / 2: # The number of iterations of j from its first run can be reduced
        if n % j == 0:
            largest_prime_factor = j
        j += 1
    return largest_prime_factor

print(largest_prime_factor.__doc__)
