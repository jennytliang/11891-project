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

  
    ans = 1
    for i in range(n):
        ans = ans * (n-i)
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
print(special_factorial(11))
print(special_factorial(12))
print(special_factorial(13))
print(special_factorial(14))
print(special_factorial(15))
print(special_factorial(16))
print(special_factorial(17))
print(special_factorial(18))
print(special_factorial(19))
print(special_factorial(20))
print(special_factorial(21))
print(special_factorial(22))
print(special_factorial(23))
print(special_factorial(24))
print(special_factorial(25))
print(special_factorial(26))
print(special_factorial(27))
print(special_factorial(28))
print(special_factorial(29))
print(special_factorial(30))
print(special_factorial(31))
print(special_factorial(32))
print(special_factorial(33))
print(special_factorial(34))
print(special_factorial(35))
print(special_factorial(36))
print(special_factorial(37))
print(special_factorial(38))
print(special_factorial(39))
print(special_factorial(40))
print(special_factorial(41))
print(special_factorial(42))
print(special_factorial(43))
print(