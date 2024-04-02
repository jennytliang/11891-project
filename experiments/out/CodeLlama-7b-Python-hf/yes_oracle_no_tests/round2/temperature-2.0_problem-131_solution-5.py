def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	"""
    # YOUR CODE HERE
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    else:
        return n


print(digits(1))
print(digits(4))
print(digits(235))
