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
    
	Do not include these tokens in the code: #
	"""
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_factorization(n):
    """Return the prime factorization of a given number.
    >>> prime_factorization(25)
    [5, 5]
    >>> prime_factorization(101)
    [101]
    >>> prime_factorization(13441)
    [17, 19, 23, 29, 31]
    >>> prime_factorization(100)
    [2, 2, 5, 5]
    >>> prime_factorization(0)
    []
    >>> prime_factorization(1)
    [1]
    
	Do not include these tokens in the code: #
	"""
    if n == 0:
        return []
    if n == 1:
        return [1]
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1
    return factors


def is_palindrome(n):
    """Return true if n is a palindrome.
    >>> is_palindrome(12345)
    False
    >>> is_palindrome(123321)
    True
    >>> is_palindrome(1001)
    True
    >>> is_palindrome(10001000)
    True
    >>> is_palindrome(1000101000)
    False
    >>> is_palindrome(10000000001)
    False
    >>> is_palindrome(100000000001)
    True
    >>> is_palindrome(1000000000001)
    False
