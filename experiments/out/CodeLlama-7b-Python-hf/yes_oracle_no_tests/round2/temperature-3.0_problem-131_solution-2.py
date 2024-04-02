def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # Your code here #
	"""
    # Your code here
    odd_digits = []
    product = 1
    while n:
        last_digit = n % 10
        if last_digit % 2 == 1:
            odd_digits.append(last_digit)
            product *= last_digit
        n //= 10
    return product


print(digits(1))
print(digits(4))
print(digits(235))
