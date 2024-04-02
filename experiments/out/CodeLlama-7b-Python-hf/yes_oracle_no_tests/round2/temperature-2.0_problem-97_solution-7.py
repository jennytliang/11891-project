def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Do not include these tokens in the code: # Return the product of their unit
	"""
    # multiply the unit digits
    return a % 10 * b % 10


if __name__ == "__main__":
    print(multiply(148, 412))  # should return 16
    print(multiply(19, 28))  # should return 72
    print(multiply(2020, 1851))  # should return 0
    print(multiply(14, -15))  # should return 20
