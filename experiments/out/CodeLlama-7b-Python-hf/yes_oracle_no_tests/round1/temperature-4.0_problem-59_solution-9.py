def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""

    largest_prime = 0
    for i in range(2, n):
        if n % i == 0:
            j = 2
            while j <= i:
                if i % j != 0:
                    j += 1
                if j == i:
                    largest_prime = i
                    break
    return largest_prime


if __name__ == "__main__":
    print("Enter number: ")
    n = int(input())
    print(largest_prime_factor(n))