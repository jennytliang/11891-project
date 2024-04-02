def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    # prime = [True] * (n+1)
    # prime[1] = False
    # for i in range(2, int(n**0.5)+1):
    #     if prime[i]:
    #         for j in range(i*i, n+1, i):
    #             prime[j] = False

    prime = [True] * (n+1)
    prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    largest_prime = 0
    for i in range(2, n+1):
        if prime[i]:
            largest_prime = i
    
    return largest_prime

if __name__ == "__main__":
    import doctest
    doctest.testmod()