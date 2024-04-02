def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: , ans
	"""

  
    # Write your code here
    ans = 1
    while n >= 1:
        ans = ans * n
        n = n - 1
    return ans


if __name__ == "__main__":
    print("Example:")
    print(special_factorial(4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert special_factorial(4) == 288
    assert special_factorial(1) == 1
    assert special_factorial(6) == 720
    assert special_factorial(12) == 479001600
    print("Coding complete? Click 'Check' to earn cool rewards!")
