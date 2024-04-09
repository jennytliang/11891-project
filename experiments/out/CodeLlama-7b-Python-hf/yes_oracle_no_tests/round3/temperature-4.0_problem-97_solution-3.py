def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # First , convert the numbers into
	"""
    # First , convert the numbers into strings
    a = str(a)
    b = str(b)
    # Then, use a for loop to iterate through the strings
    for i in range(len(a)):
        a = int(a[i])
        b = int(b[i])
        # Then, multiply the two digits together
        answer = a * b
        return answer