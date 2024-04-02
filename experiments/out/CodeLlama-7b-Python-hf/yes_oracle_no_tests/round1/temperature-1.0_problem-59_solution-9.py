def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # is_prime is a list of length (n+1), and the first element is True
    # This is because the index of the list starts from 0, and we want to check
    # if n is prime.
    is_prime = [True] * (n + 1)
    
    # The loop below marks out all the composite numbers.
    # Note that we start from 2, since 1 is not a prime.
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # The loop below finds the largest prime factor of n.
    # Note that we start from n/2, since all the numbers before n/2 are
    # prime numbers, and we only need to find the largest prime number.
    for i in range(int(n/2), 1, -1):
        if is_prime[i] and n % i == 0:
            return i

if __name__ == "__main__":
    import doctest
    doctest.testmod()