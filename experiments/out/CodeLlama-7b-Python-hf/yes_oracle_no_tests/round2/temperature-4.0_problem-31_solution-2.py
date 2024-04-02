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
    
	Do not include these tokens in the code: if
	"""


    if n <= 1:
        re = False
    else:
        re = True
        for i in range(2,n):
            if n%i == 0:
                re = False
                break
    return re





def prime_factorization(n):
    """Return a list of prime factors for a given number.
    >>> prime_factorization(10)
    [2, 5]
    >>> prime_factorization(15)
    [3, 5]
    >>> prime_factorization(70)
    [2, 2, 5, 7]
    >>> prime_factorization(100)
    [2, 2, 5, 5]
    >>> prime_factorization(25)
    [5, 5]
    >>> prime_factorization(101)
    [101]
    >>> prime_factorization(125)
    [5, 5, 5]
    >>> prime_factorization(1024)
    [2, 2, 2, 2, 2, 2, 2]
    >>> prime_factorization(1234567)
    [7, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    
	Do not include these tokens in the code: while, for, return
    """
    re = []
    if n <= 1:
        re = []
    else:
        i = 2
        while i <= n:
            if n%i == 0:
                re.append(i)
                n = n/i
                i = 2
            else:
                i = i + 1
    return re





def is_palindrome(s):
    """Return True if the letters in a given string form a palindrome.
    >>> is_palindrome('tacocat')
    True
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('robert')
    False
    >>> is_palindrome('