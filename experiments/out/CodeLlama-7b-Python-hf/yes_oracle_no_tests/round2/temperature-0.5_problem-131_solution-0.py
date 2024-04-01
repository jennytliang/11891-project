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
    # YOUR CODE HERE
    prod = 1
    for i in str(n):
        if int(i) % 2 == 1:
            prod *= int(i)
    return prod


if __name__ == '__main__':
    # These `asserts` using only for self-checking and not necessary for auto-testing
    assert digits(1) == 1, "1st example"
    assert digits(10) == 0, "2nd example"
    assert digits(111) == 3, "3rd example"
    assert digits(222) == 0, "4th example"
    assert digits(3) == 3, "5th example"
    assert digits(4) == 0, "6th example"
    assert digits(12345) == 120, "7th example"
    assert digits(987654) == 216, "8th example"
    assert digits(863754) == 120, "Small example"
    assert digits(1234567890) == 0, "Big example"
