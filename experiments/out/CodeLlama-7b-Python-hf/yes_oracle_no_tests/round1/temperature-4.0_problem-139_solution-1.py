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
    if n < 0:
        return -1
    if n == 0:
        return 1
    fac = 1
    ans = 1
    for i in range(1, n+1):
        fac *= i
        ans *= fac
    return ans

assert special_factorial(4) == 288, "First"
assert special_factorial(5) == 1814400, "Second"
assert special_factorial(6) == 14179334400, "Third"
assert special_factorial(7) == 17849532896000, "Fourth"
assert special_factorial(8) == 242782935128816000, "Fifth"
