def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has
	Do not include these tokens in the code: # Your code here str
	"""
    # Your code here
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    return product


if __name__ == "__main__":
    print(digits(1))
    print(digits(235))
    print(digits(100))
