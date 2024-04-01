def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: p
	"""
    out = 1
    for d in str(n):
        if int(d) % 2 == 1:
            out *= int(d)
    return out


if __name__ == "__main__":
    print(digits(1))
    print(digits(4))
    print(digits(235))
