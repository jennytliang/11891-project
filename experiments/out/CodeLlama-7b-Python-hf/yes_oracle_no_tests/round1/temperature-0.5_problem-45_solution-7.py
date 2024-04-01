def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
	Do not include these tokens in the code: def rectangle _ area ( a , b ):
	"""

    return a * h / 2


d = {1: 10, 2: 20, 3: 30}


def lookup(d, key):
    """
    Given a dictionary and a key, returns the value for the key
    or "Not Found" for an empty value.
    >>> d = {1: 10, 2: 20, 3: 30}
    >>> lookup(d, 1)
    10
    >>> lookup(d, 4)
    Not Found
    """
    if key in d:
        return d[key]
    return "Not Found"


def is_even(number):
    """Returns True if the number is even and False if the number is odd.
    >>> is_even(5)
    False
    >>> is_even(10)
    True
    >>> is_even(-2)
    True
    >>> is_even(0)
    True
    """
    return number % 2 == 0


def is_odd(number):
    """Returns True if the number is odd and False if the number is even.
    >>> is_odd(5)
    True
    >>> is_odd(10)
    False
    >>> is_odd(-2)
    False
    >>> is_odd(0)
    False
    """
    return number % 2 != 0


def is_prime(number):
    """Returns True if the number is a prime number and False if not.
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    >>> is_prime(-2)
    False
    >>> is_prime(0)
    False
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_palindrome(string):
    """Returns True if the string is a palindrome and False if not.
    >>> is_palindrome('tacocat')
