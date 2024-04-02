def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    for divisor in range(2,n+1):
        while n % divisor == 0:
            n = n // divisor
        if divisor > (n >> 1)+1:
            break  # since no divisor is more than half the number, as soon as 
                   # we get to the middle of the number we are done
    return divisor  # the last factor we get is the largest prime factor

