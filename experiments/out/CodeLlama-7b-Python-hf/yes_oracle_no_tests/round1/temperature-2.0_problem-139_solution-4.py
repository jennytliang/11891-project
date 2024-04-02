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
    for i in range(1, n + 1):
        fac *= i
        ans *= fac
    return ans


if __name__ == "__main__":
    print("Example:")
    print(special_factorial(4))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert special_factorial(4) == 288, "Example"
    assert special_factorial(1) == 1, "First"
    assert special_factorial(6) == 720, "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")