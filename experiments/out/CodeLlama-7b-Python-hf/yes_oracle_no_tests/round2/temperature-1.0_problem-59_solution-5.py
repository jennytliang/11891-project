def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    # 357 seconds to run 
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1): 
        if is_prime[i]:
            for num in range(i * i, n + 1, i):
                is_prime[num] = False

    i = n
    while i > 1 and not is_prime[i]:
        i -= 1

    return i

# O(sqrt(N) * N) - 38 seconds to run
def largest_prime_factor_v2(n: int):

    def get_prime_factors(num):
        i = 2
        prime_factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_factors.append(i)
        if num > 1:
            prime_factors.append(num)
        return prime_factors

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return num != 1

    candidates = get_prime_factors(n)
    candidates.sort(reverse=True)
    largest_prime_factor = 1
    for factor in candidates:
        if is_prime(factor):
            largest_prime_factor = factor
            break

    return largest_prime_factor

# O(sqrt(N)) - 45 seconds to run
def largest_prime_factor_v3(n: int):
    
    def get_prime_factors(num):
        i = 2
        prime_factors = []
        while i * i <= num:
            if num % i != 0: 
                i += 1
            else: 
                num //= i
                prime_factors.append(i)
        if num > 1:
