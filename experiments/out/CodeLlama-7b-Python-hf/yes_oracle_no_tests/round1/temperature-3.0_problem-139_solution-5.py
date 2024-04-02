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
	Do not include these tokens in the code: #
	"""
    fac = 1
    ans = 1
    for i in range(1, n):
        fac = fac * i
        ans = ans * fac
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    assert special_factorial(1) == 1, "Test 1 failed"
    assert special_factorial(2) == 2, "Test 2 failed"
    assert special_factorial(3) == 6, "Test 3 failed"
    assert special_factorial(4) == 288, "Test 4 failed"
    assert special_factorial(5) == 3840, "Test 5 failed"
    assert special_factorial(6) == 960, "Test 6 failed"
    print("Congratulations! All tests passed!")
