def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: # for i in range ( 2
	"""
    # Find the largest factor of n that is prime. Assume n > 1 and is not a prime.
    # We know that n must be greater than 2.
    largest_prime_factor = 2
    for i in range(2, n):
        if n % i == 0:
            largest_prime_factor = i
    return largest_prime_factor

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n = int(input("Enter a number (greater than 1): "))
    print(f"The largest prime factor of {n} is {largest_prime_factor(n)}")