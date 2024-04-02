def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    for i in range(2, n + 1):
        if n % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                return i

    return None


def first_n_prime_factors(n: int, number: int):
    """Return the first n prime factors of number.
    >>> first_n_prime_factors(3, 13195)
    [29, 13, 5]
    >>> first_n_prime_factors(7, 1040)
    [2, 2, 2, 5, 5, 7]
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.append(i)
                if len(factors) == n:
                    return factors

    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
