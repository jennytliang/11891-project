def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    while n % 2 == 0:
        n = n / 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            n = n / f
        f = f + 2
    return int(n)

def main():
    import doctest
    doctest.testmod()
    n = int(input("Enter a number: "))
    print(largest_prime_factor(n))

if __name__ == "__main__":
    main()