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
    
	Do not include these tokens in the code: return False # if n <
	"""



    if  n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_list(n):
    """Return a list of prime numbers less than n.
    >>> prime_list(10)
    [2, 3, 5]
    >>> prime_list(11)
    [2, 3, 5, 7]
    >>> prime_list(12)
    [2, 3, 5, 7]
    >>> prime_list(13)
    [2, 3, 5, 7, 11]
    >>> prime_list(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    return [i for i in range(2, n) if is_prime(i)]


def prime_list_2(n):
    """Return a list of prime numbers less than n.
    >>> prime_list_2(10)
    [2, 3, 5]
    >>> prime_list_2(11)
    [2, 3, 5, 7]
    >>> prime_list_2(12)
    [2, 3, 5, 7]
    >>> prime_list_2(13)
    [2, 3, 5, 7, 11]
    >>> prime_list_2(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    primes = []
    for i in range(2, n):
        if i % 2 == 0:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


def prime_list_3(