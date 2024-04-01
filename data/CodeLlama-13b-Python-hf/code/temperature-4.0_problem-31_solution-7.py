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
    """
    return all(n % i != 0 for i in range(3, int(n **0.5) +1, 2))    

def count_prims():
    n=0
    for i in range(2501):
        if is_prime(24680+i*(2*i-1)):
            n=n+1   
    return n  