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
    """ Return True if string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcdba')
    True
    >>> is_palindrome('abcdefghhgfedcba')
    True
    """
    return string == string[::-1]


def fibonacci(n: int) -> int:
    """ Return n-th Fibonacci number
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_fast(n: int) -> int:
    """ Return n-th Fibonacci number
    >>> fibonacci_fast(0)
    0
    >>> fibonacci_fast(1)
    1
    >>> fibonacci_fast(2)
    1
    >>> fibonacci_fast(3)
    2
    >>> fibonacci_fast(4)
    3
    >>> fibonacci_fast(5)
    5
    >>> fibonacci_fast(10)
    55
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_pandigital(