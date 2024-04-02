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
    
	Do not include these tokens in the code: import math
	"""
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_palindrome(s):
    """Return True if s is a palindrome, and False otherwise.
    >>> is_palindrome('tacocat')
    True
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('robert')
    False
    >>> is_palindrome('kayak')
    True
    >>> is_palindrome('hello')
    False
    >>> is_palindrome('a')
    True
    >>> is_palindrome('')
    True
    """
    return s == s[::-1]


def is_list_permutation(L1, L2):
    """Returns True if L1 and L2 are permutations of each other.
    >>> is_list_permutation([1, 2, 3], [2, 1, 3])
    True
    >>> is_list_permutation([1, 2, 3], [2, 1, 3, 4])
    False
    >>> is_list_permutation([1, 2, 1], [2, 1, 1])
    False
    >>> is_list_permutation([1, 2, 3, 4], [7, 8, 9, 10])
    False
    >>> is_list_permutation([], [])
    True
    """
    if len(L1) != len(L2):
        return False
    return sorted(L1) == sorted(L2)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    1