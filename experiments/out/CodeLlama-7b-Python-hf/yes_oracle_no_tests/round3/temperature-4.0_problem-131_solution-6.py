def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd ,
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 0
    else:
        product = 1
        while n > 0:
            digit = n % 10
            if digit % 2 == 1:
                product = product * digit
            n = n // 10
        return product


if __name__ == "__main__":
    print(digits(0))
    # 0

    print(digits(1))
    # 1

    print(digits(4))
    # 0

    print(digits(102))
    # 0

    print(digits(235))
    # 15
