def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    is_prime = [True] * (n + 1)
    for i in range(2, n):
        if is_prime[i]:
            for j in range(i, n, i):
                is_prime[j] = False
    for i in reversed(range(2, n)):
        if is_prime[i] and n % i == 0:
            return i
    raise ValueError("n must be greater than 1 and not prime")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(600851475143))
