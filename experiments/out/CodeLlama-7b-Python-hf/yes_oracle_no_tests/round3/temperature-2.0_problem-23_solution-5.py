def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return True if the given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcb')
    False
    >>> is_palindrome('abcdba')
    False
    >>> is_palindrome('abcdcba')
    False
    """
    return string == string[::-1]


def gcd(a: int, b: int) -> int:
    """ Return the greatest common divisor of two numbers
    >>> gcd(0, 0)
    0
    >>> gcd(1, 0)
    1
    >>> gcd(0, 1)
    1
    >>> gcd(4, 2)
    2
    >>> gcd(4, 6)
    2
    >>> gcd(2, 6)
    2
    >>> gcd(10, 12)
    2
    >>> gcd(10, 15)
    5
    >>> gcd(10, 16)
    1
    >>> gcd(10, 17)
    1
    """
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b % a, a)


def list_prod(lst: list) -> int:
    """ Return the product of all the elements in a list
    >>> list_prod([1, 2])
    2
    >>> list_prod([1, 2, 3])
    6
    >>> list_prod([1, 2, 3, 4])
    24
    """
    if len(lst) == 0:
        return 1