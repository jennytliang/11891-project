def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # for i in range(2, n):
    #     while n % i == 0:
    #         n = n // i
    #         is_prime[i] = False
    # return n
    # is_prime = [True] * (n + 1)
    # is_prime[0] = is_prime[1] = False
    # for i in range(2, n + 1):
    #     if is_prime[i]:
    #         for j in range(i * 2, n + 1, i):
    #             is_prime[j] = False
    # largest_prime = 0
    # for i in range(2, n + 1):
    #     if is_prime[i]:
    #         largest_prime = i
    # return largest_prime
    # is_prime = [True] * (n + 1)
    # is_prime[0] = is_prime[1] = False
    # for i in range(2, n + 1):
    #     if is_prime[i]:
    #         for j in range(i * 2, n + 1, i):
    #             is_prime[j] = False
    # largest_prime = 0
    # for i in range(2, n + 1):
    #     if is_prime[i]:
    #         largest_prime = i
    # return largest_prime

    # is_prime = [True] * (n + 1)
    # is_prime[0] = is_prime[1] = False
    # for i in range(2, n + 1):
    #     if is_prime[i]:
    #         for j in range(i * 2, n + 1, i):
    #             is_prime[j] = False
    # largest_prime = 0
    # for i in range(2, n + 1):
    #     if is_prime[i]:
    #         largest_prime = i
    # return largest_prime

    is_prime = [True] * (n + 