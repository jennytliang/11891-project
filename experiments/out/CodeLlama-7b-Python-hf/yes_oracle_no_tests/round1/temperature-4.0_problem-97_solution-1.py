def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int
	Do not include these tokens in the code: if not any ([ type
	"""
    # First, convert to strings
    a = str(a)
    b = str(b)

    # Then, get the last digits of each
    a = int(a[-1])
    b = int(b[-1])

    # Multiply them
    c = a * b

    # Return the last digit of the product
    return c
