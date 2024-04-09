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
    # check if n is even
    if n % 2 == 0:
        return 0
    # if n is odd, check if it has odd digits
    # if it has odd digits, then do the following:
    if n % 10 % 2 == 1:
        prod = n % 10
        while n > 0:
            # if n has odd digit, then divide the number by 10
            n = n // 10
            # if n has even digit, then multiply the number by 10
            n = n * 10
        return prod


print(digits(1))
print(digits(4))
print(digits(235))
print(digits(1234567890))
