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
	Do not include these tokens in the code: if n ==
	"""

    i = 1
    fac = 1
    while i <= n:
        fac = fac * i
        i = i + 1
    ans = fac

    i = 1
    while i <= n-1:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-2:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-3:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-4:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-5:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-6:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-7:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-8:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-9:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    i = 1
    while i <= n-10:
        fac = fac * (n-i)
        i = i + 1
    ans = ans * fac

    return ans

