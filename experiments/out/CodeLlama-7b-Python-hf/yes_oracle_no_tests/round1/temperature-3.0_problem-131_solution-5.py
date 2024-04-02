def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    result = 1
    for d in str(n):
        if int(d) % 2 == 1:
            result *= int(d)
    return result


assert digits(1) == 1, "digits(1) == 1"
assert digits(5) == 5, "digits(5) == 5"
assert digits(10) == 0, "digits(10) == 0"
assert digits(101) == 1, "digits(101) == 1"
assert digits(222) == 0, "digits(222) == 0"
assert digits(123456789) == 126, "digits(123456789) == 126"
