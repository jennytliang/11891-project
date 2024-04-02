def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # BEGIN PROBLEM 2
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
        else:
            prod *= 1
    return prod
    # END PROBLEM 2


def is_palindrome(n):
    """Returns True if n is a palindrome and False otherwise.

    Hint: use digits() and string multiplication

    >>> is_palindrome(5)
    False
    >>> is_palindrome(121)
    True
    >>> is_palindrome(1221)
    True
    >>> is_palindrome(72827)
    True
    >>> is_palindrome(585)
    True
    """
    # BEGIN PROBLEM 3
    return digits(n) == digits(n)
    # END PROBLEM 3


def summation(n, term):
    """Returns the sum of terms 1 through n (i.e., 1+2+...+n)
    using the formula

         n * (n + 1) / 2

    For example,

    >>> summation(5, lambda x: x)
    15
    >>> summation(1, lambda x: 2*x)
    2
    >>> summation(100, lambda x: x)
    5050
    """
    assert n >= 1
    # BEGIN PROBLEM 4
    return n * (n + 1) / 2
    # END PROBLEM 4


def product(n, term):
    """Returns the product of terms 1 through n (i.e., 1*2*...*n)
    using the formula

         n * (n - 1) * ... * 1

    For example,

    >>> product(4, lambda x: x)
    24
    >>> product(6, lambda x: x + 1)
    132
    >>> product