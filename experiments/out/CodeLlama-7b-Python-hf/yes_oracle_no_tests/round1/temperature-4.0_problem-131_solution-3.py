def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prod = True
        for i in range(len(str(n))):
            if int(str(n)[i]) % 2 == 0:
                prod = False
                break
        if prod == True:
            return n
        else:
            return 0


def digits1(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	"""
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 if n % 2 else 0
