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
    result = 1
    for i in range(n):
        result = result * (n - i)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
