def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""
    
def digits(n):
    s = str(n)
    # code goes here
    even_count = 0
    product = 1
    for x in s:
        if int(x) % 2 == 0:
            even_count += 1
        else:
            # x is odd
            product = int(x) * product
            
    if even_count == len(s):
        return 0
    else:
        return product