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
    # First, convert the numbers into strings
    str_a = str(a)
    str_b = str(b)
    
    # Next, extract the last digit of each number and multiply them together
    last_digit_a = int(str_a[-1])
    last_digit_b = int(str_b[-1])
    last_product = last_digit_a * last_digit_b
    
    # Then, return the last product
    return last_product


# print(multiply(148, 412)) # should return 16
# print(multiply(19, 28)) # should return 72
# print(multiply(2020, 1851)) # should return 0
# print(multiply(14,-15)) # should return 20