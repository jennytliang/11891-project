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

    if n == 0:
        return 0

    if n % 2 == 0:
        return 0

    if n < 10:
        return n

    if n % 10 == 0:
        return 0

    if n % 10 != 0:
        if n % 2 == 0:
            return 0
        else:
            return n % 10 * digits(n // 10)









































































