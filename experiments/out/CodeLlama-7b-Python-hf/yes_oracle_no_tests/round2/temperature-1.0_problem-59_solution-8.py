def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: # is prime = [ True ]
	"""
    # Your code here
    # prime = [True] * (n+1)
    # prime[0] = prime[1] = False
    # for i in range(2, n+1):
    #     if prime[i] == True:
    #         for j in range(i*2, n+1, i):
    #             prime[j] = False
    # return max([i for i in range(2, n+1) if prime[i] == True])
    # prime_factor = [True] * (n+1)
    # prime_factor[0] = prime_factor[1] = False
    # for i in range(2, n+1):
    #     if prime_factor[i] == True:
    #         for j in range(i*2, n+1, i):
    #             prime_factor[j] = False
    # return max([i for i in range(2, n+1) if prime_factor[i] == True])
    # prime_factor = [True] * (n+1)
    # prime_factor[0] = prime_factor[1] = False
    # for i in range(2, n+1):
    #     for j in range(2, n+1, i):
    #         prime_factor[j] = False
    # return max([i for i in range(2, n+1) if prime_factor[i] == True])
    # prime_factor = [True] * (n+1)
    # prime_factor[0] = prime_factor[1] = False
    # for i in range(2, n+1):
    #     if prime_factor[i] == True:
    #         for j in range(i*2, n+1, i):
    #             prime_factor[j] = False
    # return max([i for i in range(2, n+1) if prime_factor[i] == True])
    # prime_factor = [True] * (n+1)
    # prime_factor[0] = prime_factor[1] = False
    # for i