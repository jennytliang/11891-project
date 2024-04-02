def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    #largest_prime_factor = 1
    #for num in range(2,n+1):
    #    if n % num == 0:
    #        largest_prime_factor = num
    #        break
    #return largest_prime_factor
    largest_prime_factor = 1
    for num in range(2, n):
        if n % num == 0:
            largest_prime_factor = num
    return largest_prime_factor


def unique_digits(n: int):
    """Return the set of digits that appear in n.
    >>> unique_digits(8675309)
    {6, 7, 8, 9, 0}
    >>> unique_digits(12345)
    {1, 2, 3, 4, 5}
    >>> unique_digits(111111)
    {1}
    >>> unique_digits(123789)
    {1, 2, 3, 7, 8, 9}
    """
    "*** YOUR CODE HERE ***"
    #unique_digits = set()
    #while n != 0:
    #    unique_digits.add(n % 10)
    #    n = n // 10
    #return unique_digits
    num_str = str(n)
    return set(int(char) for char in num_str)


def digital_root(n: int):
    """Return the digital root of n, recursively.
    >>> digital_root(1655)
    6
    >>> digital_root(942)
    6
    >>> digital_root(123456789)
    9
    """
    "*** YOUR CODE HERE ***"
    #digital_root = 0
    #while n != 0:
    #    digital_root += n % 10
    #    n = n // 10
    #return digital