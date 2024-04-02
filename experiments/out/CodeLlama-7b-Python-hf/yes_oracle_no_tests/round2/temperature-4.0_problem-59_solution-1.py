def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    "*** YOUR CODE HERE ***"
    # for i in range(2, n+1):
    #     if n % i == 0 and is_prime(i):
    #         return i
    # return n

    # Approach 1
    # while n > 1:
    #     for i in range(2, n+1):
    #         if n % i == 0 and is_prime(i):
    #             return i
    #     n -= 1
    # return n

    # Approach 2
    # for i in range(2, n+1):
    #     if n % i == 0 and is_prime(i):
    #         n //= i
    # return n

    # Approach 3
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0 and is_prime(i):
                n //= i
                break
    return n


def is_prime(n: int):
    """Returns True if n is a prime number, otherwise False.
    >>> is_prime(132)
    False
    >>> is_prime(121)
    True
    >>> is_prime(123)
    False
    >>> is_prime(11)
    True
    >>> is_prime(1)
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n+1, 2):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n: int):
    """Returns the sum of the digits of n.
    >>> sum_of_digits(10) # 1 + 0 = 1
    1
    >>> sum_of_digits(4224) # 4 + 2 + 2 + 4 = 1