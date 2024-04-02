def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # Check if n is a prime number
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    # Loop through all numbers n/2 and check if n % i == 0
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False
    # Find the largest prime factor
    # For the numbers below 10, the largest prime factor is the number itself
    largest_prime = n
    for i in range(n - 1, 1, -1):
        if is_prime[i]:
            largest_prime = i
            break
    return largest_prime


if __name__ == "__main__":
    import doctest

    doctest.testmod()
