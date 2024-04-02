def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    primes_flag = [True] * (n + 1)
    primes_flag[0] = False
    primes_flag[1] = False
    for i in range(2,n+1):
        if primes_flag[i] == True:
            for j in range(2*i,n+1,i):
                primes_flag[j] = False
    for i in range(2,n+1):
        if primes_flag[i] == False and n % i == 0:
            return i
    return n

def main():
    print(largest_prime_factor(13195))
    print(largest_prime_factor(2048))

### LAB 2.7.3 PRIME FACTORS AND PRIMES - STRETCH AND BONUS
# Add this code that returns the prime factors of n using memoization:
# The key is the number the numbers that have already be calculated
# The values are the prime_factors we've already calculated
def memoized_largest_prime_factor(n,d={}):
    """Return the largest prime factor of n.  Assume n > 0.
    >>> memoized_largest_prime_factor(13195)
    29
    >>> memoized_largest_prime_factor(600851475143)
    6857

	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    if n in d:
        return d[n]
    else:
        primes_flag = [True] * (n + 1)
        primes_flag[0] = False
        primes_flag[1] = False
        for i in range(2,n+1):
            if primes_flag[i] == True:
                for j in range(2*i,n+1,i):
                    primes_flag[j