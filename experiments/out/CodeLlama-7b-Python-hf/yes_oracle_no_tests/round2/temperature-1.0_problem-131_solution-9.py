def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod = False ,
	"""
    
    
    odd_digits = [num for num in map(int, str(n)) if num % 2 != 0]
    
    if len(odd_digits) == 0:
        return 0
    
    odd_digits_product = 1

    for digit in odd_digits:
        odd_digits_product *= digit 
    
    return odd_digits_product