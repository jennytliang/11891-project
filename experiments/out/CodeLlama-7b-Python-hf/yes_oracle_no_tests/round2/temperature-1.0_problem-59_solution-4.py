def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	"""

    # TODO: write a solution here
    # Hint: You can use the is_prime function to check if a number is prime
    largest = 0
    for i in range(2, n + 1):
        if n % i == 0:
            if is_prime(i):
                largest = i
    return largest


def is_prime(n: int):
    """Return True if n is a prime number, False otherwise.
    >>> is_prime(13195)
    False
    >>> is_prime(2048)
    True
    >>> is_prime(11)
    True
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(73)
    True
    """

    # TODO: write a solution here
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(13195))
