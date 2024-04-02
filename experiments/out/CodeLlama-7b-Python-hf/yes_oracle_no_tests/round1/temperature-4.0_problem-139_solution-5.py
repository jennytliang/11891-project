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
    for i in range(1, n+1):
        fac *= i
        ans *= fac
    return ans


print(special_factorial(1))
print(special_factorial(2))
print(special_factorial(3))
print(special_factorial(4))
print(special_factorial(5))
print(special_factorial(6))
print(special_factorial(7))
print(special_factorial(8))
print(special_factorial(9))
print(special_factorial(10))
