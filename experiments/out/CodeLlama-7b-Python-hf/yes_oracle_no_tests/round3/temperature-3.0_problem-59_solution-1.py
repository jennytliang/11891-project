def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # Initialize a list of size n (to use list indexing)
    is_prime = [True] * (n + 1)
    # Set 0 and 1 to not prime
    is_prime[0] = is_prime[1] = False
    # Loop through all numbers from 2 to n
    for i in range(2, n + 1):
        # If the number is prime
        if is_prime[i]:
            # Loop through all numbers between i and n, by i increments
            for j in range(i, n + 1, i):
                # Set the number to not prime
                is_prime[j] = False
    # Loop through all numbers from n to 2, by -1 increments
    for i in range(n, 1, -1):
        # If the number is prime
        if is_prime[i]:
            # Return the number
            return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(largest_prime_factor(13195))
