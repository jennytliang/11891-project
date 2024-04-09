def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: n _ sqrt
	Do not include these tokens in the code: sq rt
	"""


    if n <= 1:
        reutrn False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def main():
    import doctest
    doctest.testmod()
    print("Done!")

if __name__ == "__main__":
    main()