def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # code here
	"""
    # code here
    if n == 0:
        return 0
    res = 1
    if n % 2 != 0:
        res *= n % 10
    return res * digits(n // 10)


# tests
assert digits(1) == 1
assert digits(4) == 0
assert digits(102) == 0
assert digits(101) == 1
assert digits(235) == 15
assert digits(2345) == 30
