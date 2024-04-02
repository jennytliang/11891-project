def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd
	Do not include these tokens in the code: # your code here #
	"""
    # your code here
    result = 1
    for i in str(n):
        if int(i) % 2 == 1:
            result *= int(i)
    return result


print(digits(1))
print(digits(4))
print(digits(235))
print(digits(123456789))
print(digits(101))
print(digits(1234567890))
print(digits(10101))
print(digits(235))
print(digits(0))
print(digits(12345678900))
