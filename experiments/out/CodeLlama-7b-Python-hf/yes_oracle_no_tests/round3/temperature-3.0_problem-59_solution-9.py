def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Do not include these tokens in the code: _
	"""

  # Your code here
    if n == 1:
        return 1

    for i in range(2, n + 1):
        while n % i == 0:
            n /= i
        if n == 1:
            return i

        if i == 2:
            continue
        if i % 2 == 0:
            i += 1
        else:
            i += 2

    return n


if __name__ == "__main__":
    print("Largest Prime Factor:", largest_prime_factor(13195))
    print("Largest Prime Factor:", largest_prime_factor(2048))