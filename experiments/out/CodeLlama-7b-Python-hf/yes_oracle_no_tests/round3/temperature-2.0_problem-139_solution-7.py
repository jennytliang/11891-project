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
    # This is a special case
    if n == 0:
        return 1

    # Initialize the ans
    ans = 1

    # Calculate the special factorial
    for i in range(n, 0, -1):
        ans = ans * i

    return ans


print(special_factorial(4))
