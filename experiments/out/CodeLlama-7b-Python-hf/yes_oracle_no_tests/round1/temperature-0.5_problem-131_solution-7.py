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
    for d in str(n):
        if int(d) % 2 != 0:
            p *= int(d)
    return p


# print(digits(1))
# print(digits(4))
# print(digits(235))
# print(digits(123456789))


def digits2(n):
    """Given a positive integer n, return the sum of the digits.
    For example:
    digits(1)  == 1
    digits(4)  == 4
    digits(235) == 8
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""

    s = 0
    for d in str(n):
        s += int(d)
    return s


# print(digits2(1))
# print(digits2(4))
# print(digits2(235))
# print(digits2(123456789))


def digits3(n):
    """Given a positive integer n, return the sum of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 4
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: product
	"""

    s = 0
    for d in str(n):
        if int(d) % 2 != 0:
            s += int(d)
    return s


# print(digits3(1))
# print(digits3(4))
# print(digits3(235))
# print(digits3(123456789))


def digits4(n):
    """Given a positive integer n, return the sum of the even digits.
    Return 0 if all digits are odd.
