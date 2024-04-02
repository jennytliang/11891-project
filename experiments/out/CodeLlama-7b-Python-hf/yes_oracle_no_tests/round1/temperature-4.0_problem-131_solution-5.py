def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # This is a solution using a loop
    # prod = 1
    # for digit in str(n):
    #     if int(digit) % 2 == 1:
    #         prod *= int(digit)
    # return prod

    # This is a solution using recursion
    prod = 1
    if n == 0:
        return 0
    elif n % 2 == 1:
        return n
    else:
        return digits(n // 10) * digits(n % 10)
