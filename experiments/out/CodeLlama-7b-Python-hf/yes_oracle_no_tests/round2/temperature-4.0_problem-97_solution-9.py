def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: int ( str (
	"""

    r = str(a)[-1] * b
    s = str(b)[-1] * a
    return int(r) + int(s)


print(multiply(148, 412))
print(multiply(19, 28))
print(multiply(2020, 1851))
print(multiply(14, -15))
