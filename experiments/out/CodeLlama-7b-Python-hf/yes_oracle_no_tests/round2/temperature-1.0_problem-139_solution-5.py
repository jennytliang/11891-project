def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: fac , ans =
	"""
    fac = n
    ans = 1
    while fac > 0:
        ans *= fac
        fac -= 1
    return ans


if __name__ == "__main__":
    import doctest
    doctest.testmod()
