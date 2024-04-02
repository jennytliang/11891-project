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
	Do not include these tokens in the code: #
	"""

    fac = 1
    ans = 1
    while fac <= n:
        ans = ans * fac
        fac += 1
    return ans
