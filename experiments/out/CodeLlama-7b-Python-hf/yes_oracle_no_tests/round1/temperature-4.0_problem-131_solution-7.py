def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    # your code here
    #prod = 1
    #for x in range(1, n+1):
    #    if x % 2 == 1:
    #        prod *= x
    #return prod
    prod = 0
    for x in range(1, n+1):
        if x % 2 == 1:
            prod *= x
    return prod

#print(digits(1))
#print(digits(4))
#print(digits(235))
#print(digits(12345))
#print(digits(100000))

def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    prod = 1
    for x in str(n):
        if int(x) % 2 == 1:
            prod *= int(x)
    return prod

#print(digits(1))
#print(digits(4))
#print(digits(235))
#print(digits(12345))
#print(digits(100000))
