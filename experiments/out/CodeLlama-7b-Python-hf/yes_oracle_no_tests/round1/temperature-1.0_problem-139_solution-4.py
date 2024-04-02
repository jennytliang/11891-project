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
    a = 1
    b = 0
    fac=1
    ans=0
    while n>=b:
        a+=1
        b=a
        print(a)        
        while abs(b)!=inf:
            fac=fac*b
            print(fac)
            b-=1
    return (2**(2*n*(((n//2)+1))+(n/2)))*fac

