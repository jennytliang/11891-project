def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""

    # Your code here
    if n <= 1:
        return None
    largest = 1
    while n % 2 == 0:
        largest = 2
        n = n / 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest = i
            n = n / i
    if n > 2:
        largest = n
    return largest


if __name__ == "__main__":
    import doctest
    doctest.testmod()