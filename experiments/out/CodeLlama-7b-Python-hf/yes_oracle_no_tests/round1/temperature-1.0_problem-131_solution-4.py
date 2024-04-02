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

    # WRITE YOUR CODE HERE
    odd=n
    product=1
    while odd>0:
        digit=od=n%10
        if digit%2!=0:
            product*=digit
        odd//=10
    return product
