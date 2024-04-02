def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    number = n
    product = 1
    while number > 0:
        digit = number % 10
        if digit % 2 == 1:
            product *= digit
        number = number // 10
    return product


print(digits(123))
