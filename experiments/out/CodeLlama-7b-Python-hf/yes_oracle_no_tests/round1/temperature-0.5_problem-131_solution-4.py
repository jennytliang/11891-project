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

    p = 1
    while n > 0:
        if n % 2 == 1:
            p *= n % 10
        n = n // 10
    return p


# print(digits(1))
# print(digits(4))
# print(digits(235))
# print(digits(1001))
# print(digits(10011))
# print(digits(9999999999))


def digits2(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""

    p = 1
    while n > 0:
        if n % 2 == 1:
            p *= n % 10
        n = n // 10
    return p


print(digits(1))
print(digits(4))
print(digits(235))
print(digits(1001))
print(digits(10011))
print(digits(9999999999))


def digits3(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""

    p = 1
    while n > 0:
        if n % 2 == 1:
            p *= n % 10
        n = n // 10
    return p
