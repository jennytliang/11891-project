def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n*special_factorial(n-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
