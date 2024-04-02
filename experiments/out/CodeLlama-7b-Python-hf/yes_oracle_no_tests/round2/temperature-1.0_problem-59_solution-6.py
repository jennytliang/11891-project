def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: #
	"""
    # your code here
    prime = n
    for i in range(2, n):
        if n % i == 0:
            prime = i
            n = n / i
            if n == 1:
                return prime

