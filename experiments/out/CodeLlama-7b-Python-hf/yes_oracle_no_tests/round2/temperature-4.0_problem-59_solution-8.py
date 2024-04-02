def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    largest = n
    while (n > 1):
        i = 2
        while (i <= n):
            if (n % i == 0):
                n = n // i
                break
            i += 1
        if (i == n + 1):
            break
    return largest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(13195))
    print(largest_prime_factor(2048))
    print(largest_prime_factor(13195))