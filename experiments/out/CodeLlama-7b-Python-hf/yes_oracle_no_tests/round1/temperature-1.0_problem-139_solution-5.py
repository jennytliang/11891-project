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
    while n > 0:
        fac *= n
        n -= 1
        ans *= fac
    return ans


if __name__ == "__main__":
    print("Example:")
    print(special_factorial(4))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert special_factorial(4) == 288, "4!"
    assert special_factorial(1) == 1, "1!"
    assert special_factorial(6) == 720, "6!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
