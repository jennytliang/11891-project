def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # A list of primes.
    primes = list()
    # Iterate over the range of numbers.
    for num in range(2, n + 1):
        # Assume every number is prime until proven otherwise.
        is_prime = True
        # Check if the number is divisible by any number in the list.
        for prime in primes:
            if num % prime == 0:
                # If it is divisible, then it is not prime.
                is_prime = False
                break
        # If it is prime, add it to the list.
        if is_prime:
            primes.append(num)
    # Return the last element of the list.
    return primes[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()