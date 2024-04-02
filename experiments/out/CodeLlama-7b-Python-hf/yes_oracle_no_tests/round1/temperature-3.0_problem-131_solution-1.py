def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    if n == 0:
        return 0
    prod = True
    for d in str(n):
        if int(d) % 2 == 1:
            if prod == False:
                return 0
            prod = True
        else:
            if prod == True:
                return 0
            prod = False
    return prod


print(digits(1))
print(digits(4))
print(digits(235))
