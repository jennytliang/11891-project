def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""

    # Initialize a list of booleans to keep track of which numbers are prime.
    is_prime = [True] * (n + 1)

    # Since 1 does not count as a prime factor, mark 1 as not prime.
    is_prime[1] = False

    # Loop over all odd integers from 3 to n + 1.
    for i in range(3, n + 1, 2):
        # Check if i is prime.
        if is_prime[i]:
            # Loop over all odd integers i * j from i * i to n + 1.
            for j in range(i * i, n + 1, i):
                # Mark j as composite.
                is_prime[j] = False

    # Loop over all numbers from 2 to n.
    for i in range(2, n + 1):
        # If i is prime, return i.
        if is_prime[i]:
            return i
