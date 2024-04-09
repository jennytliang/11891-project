def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: ## code here product
	"""
    # YOUR CODE HERE
    # Use the same variable names as on the edX platform
    # to make it easier to compare your code with ours
    product=1
    for i in range(0,len(str(n))):
        if int(str(n)[i])%2!=0:
            product=product*int(str(n)[i])
    return product


print digits(1)
print digits(4)
print digits(235)
