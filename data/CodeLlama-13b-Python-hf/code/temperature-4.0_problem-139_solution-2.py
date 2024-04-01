def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # base case
    if n<=0:
        raise ValueError('input n must be positive')
    # recurse
    elif n>1:
        return n*special_factorial(n-1)
#     alternatively you can add an exit case to handle
#     edge cases:
#     elif n>0&n==1: return 1 
        

if __name__=='__main__':
    import doctest