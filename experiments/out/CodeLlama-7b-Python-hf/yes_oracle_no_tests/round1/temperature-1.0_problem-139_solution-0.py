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
    
    if n == 0:
        return "0!"
    ans = 1
    i = 1
    while i <= n:
        if i == 1:
            fac = i
        else:
            fac = fac*i
        i += 1
    return fac
