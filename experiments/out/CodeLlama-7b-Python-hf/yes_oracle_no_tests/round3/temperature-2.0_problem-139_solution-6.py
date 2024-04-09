def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: fac ,
	Do not include these tokens in the code: # Write your code
	"""
    fac=1
    for i in range(n,0,-1):
        fac=fac*i
    return fac

print(special_factorial(4))
