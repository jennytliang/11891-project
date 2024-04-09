def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n-1)
    
    
def sum_to_n_recursive(n: int):
    """sum_to_n_recursive is a function that sums numbers from 1 to n.
    >>> sum_to_n_recursive(30)
    465
    >>> sum_to_n_recursive(100)
    5050
    >>> sum_to_n_recursive(5)
    15
    >>> sum_to_n_recursive(10)
    55
    >>> sum_to_n_recursive(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    return n
    
    
def is_prime(n: int):
    """is_prime is a function that returns True if n is prime and False if not.
    >>> is_prime(3)
    True
    >>> is_prime(6)
    False
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    >>> is_prime(11)
    True
    >>> is_prime(10)
    False
    
	Include these tokens in the code: if ( n == 2 or n == 3 or
    """
    return True
    
    
def factorial(n: int):
    """factorial is a function that returns n!
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    
	Include these tokens in the code: if ( n == 0 or n == 1 or
    """
    return 1
    
    
def reverse(s: str):
    """reverse is a function that reverses the string s.
    >>> reverse("abc")
    "cba"
    >>> reverse("123456789")
    "987654321"