def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    # *** YOUR CODE HERE ***
    # Hint: 2 is the only even prime number
    if n == 2:
        return 2
    # Hint: 2 is the only even prime number
    if n % 2 == 0:
        n = n // 2
    # Hint: 2 is the only even prime number
    if n % 2 == 0:
        return 2
    # Hint: 2 is the only even prime number
    while n % 2 == 0:
        n = n // 2
    # Hint: 3 is the only odd prime number
    if n % 3 == 0:
        return 3
    while n % 3 == 0:
        n = n // 3
    i = 5
    # Hint: 5 is the first prime number greater than 2
    while i * i <= n:
        if n % i == 0:
            return i
        while n % i == 0:
            n = n // i
        i += 2
    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()