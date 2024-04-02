def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""
    # YOUR CODE HERE
    largest_prime = 1
    for i in range(2, n):
        if n % i == 0:
            largest_prime = i
            break
    return largest_prime