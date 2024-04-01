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
    i = 3
    while (i * i) <= (n - 1):
        if n % i == 0:
            print "This is not prime"
            return False;
        i = i + 2
    print "This is also prime"      
    if n < 5:
       return False
    print "is prime"
    return False