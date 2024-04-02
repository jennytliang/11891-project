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

    fac = 1
    ans = 1
    
    for number in range(n):
        
        fac = fac * (number + 1)
        ans = ans * fac

    ans = ans % 2435

    return ans + 1
