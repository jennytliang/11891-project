def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""

    # YOUR CODE HERE
    if n % 2 == 0:
        largest_prime_factor = 2
    else:
        largest_prime_factor = 1
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime_factor = i
            n = n / i
        i += 2
    return largest_prime_factor

print(largest_prime_factor(13195))
print(largest_prime_factor(2048))