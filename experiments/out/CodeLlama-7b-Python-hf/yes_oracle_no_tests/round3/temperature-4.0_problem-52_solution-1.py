def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x < t:
            return True
    return False

def sum_multiples(n: int, thresh: int):
    """Return the sum of all multiples of n below threshold thresh.
    >>> sum_multiples(3, 10)
    30
    >>> sum_multiples(5, 6)
    0
    >>> sum_multiples(7, 50)
    105
    """
    s = 0
    for i in range(thresh//n):
        s += i*n
    return s

def sum_multiples_below(n: int, thresh: int):
    """Return the sum of all multiples of n below threshold thresh.
    >>> sum_multiples_below(3, 10)
    30
    >>> sum_multiples_below(5, 6)
    0
    >>> sum_multiples_below(7, 50)
    105
    """
    s = 0
    for i in range(thresh//n):
        if i*n < thresh:
            s += i*n
    return s

def factorial(n: int):
    """Return n factorial.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n: int):
    """Returns True if n is a prime number.

    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(521)
    True
    """
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def prime_sum(n: int):
    """Returns the sum