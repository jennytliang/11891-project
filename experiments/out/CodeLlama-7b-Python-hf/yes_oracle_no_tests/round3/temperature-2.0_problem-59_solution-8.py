def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    largest_prime_factor = 1
    for i in range(2, n+1):
        if n % i == 0:
            is_prime = True
            for j in range(2, i//2+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                largest_prime_factor = i
                break
    return largest_prime_factor


def smallest_prime_factor(n: int):
    """Return the smallest prime factor of n. Assume n > 1 and is not a prime.
    >>> smallest_prime_factor(13195)
    1981
    
    Include these tokens in the code: is prime = [ True ] * ( n +
    """
    "*** YOUR CODE HERE ***"
    smallest_prime_factor = 1
    for i in range(2, n+1):
        if n % i == 0:
            is_prime = True
            for j in range(2, i//2+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                smallest_prime_factor = i
                break
    return smallest_prime_factor
