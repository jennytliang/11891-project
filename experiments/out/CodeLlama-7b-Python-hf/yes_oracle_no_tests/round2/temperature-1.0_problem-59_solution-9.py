def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # is_prime = is_prime_1[:]
    if n <= 3: return n
    else: is_prime = [True for _ in range(n+1)] 
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i] and i*i <= n:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return int(sorted(p for p in range(2, n+1) if is_prime[p])[-1])

print(largest_prime_factor(600851475143))
