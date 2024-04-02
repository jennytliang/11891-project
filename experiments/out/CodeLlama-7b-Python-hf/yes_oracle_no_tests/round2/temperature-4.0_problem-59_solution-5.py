def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(2, n // i + 1):
                prime[i * j] = False
    return max(i for i in range(2, n + 1) if prime[i])


def main():
    examples = [13195, 2048]
    for n in examples:
        print('Largest prime factor of', n, 'is', largest_prime_factor(n))


if __name__ == '__main__':
    main()