def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """

def is_prime(x: int):
    """
    Checks if given value is an integer prime number
    >>> assert is_prime(13), "Prime number is not recognized as prime"
    >>> assert is_prime(43043), "Not prime number are recognized as prime"
    """

def print_primes_in_interval(left: int, right: int):#ok
    """
    Iterating through all possible numbers in given range prints to screen
    >>> print_primes_in_interval(-1, 100)
    Number -1 is NOT prime
    2 is a prime number
    3 is a new prime number
    5 is a prime number
