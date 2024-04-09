def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)

print(strlen(''))
print(strlen('abc'))

def is_palindrome(string: str) -> bool:
    """ Return whether given string is palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abc')
    False
    
    Include these tokens in the code: string == string [ :: -1 ]
	"""
    return string == string[::-1]

print(is_palindrome(''))
print(is_palindrome('aba'))
print(is_palindrome('abc'))

def fib(n: int) -> int:
    """ Return the n-th Fibonacci number
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    
    Include these tokens in the code:
    if n <= 1: return n
    else: return fib(n - 1) + fib(n - 2)
    """
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

def is_prime(n: int) -> bool:
    """ Return whether given number is prime
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    
    Include these tokens in the code:
    if n <= 1: return False
    for i in range(2, n // 