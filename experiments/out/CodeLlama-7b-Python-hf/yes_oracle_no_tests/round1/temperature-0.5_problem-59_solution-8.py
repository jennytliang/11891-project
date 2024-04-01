def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code:  " *** Y OUR CO DE H ERE ***
	"""

    while n % 2 == 0:
        n = n // 2
    while n % 3 == 0:
        n = n // 3
    while n % 5 == 0:
        n = n // 5
    while n % 7 == 0:
        n = n // 7
    while n % 11 == 0:
        n = n // 11
    while n % 13 == 0:
        n = n // 13
    while n % 17 == 0:
        n = n // 17
    while n % 19 == 0:
        n = n // 19
    while n % 23 == 0:
        n = n // 23
    while n % 29 == 0:
        n = n // 29
    return n


if __name__ == "__main__":
    print("Example:")
    print(largest_prime_factor(13195))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(2048) == 2
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(315) == 5
    assert largest_prime_factor(42) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")