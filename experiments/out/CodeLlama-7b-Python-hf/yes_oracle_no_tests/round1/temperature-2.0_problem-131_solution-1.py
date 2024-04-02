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
    # Your code here
    odd=0
    prod=1
    while n>0:
        if n%2!=0:
            odd=n%10
            prod=prod*odd
        n=n//10
    return prod

print(digits(123))