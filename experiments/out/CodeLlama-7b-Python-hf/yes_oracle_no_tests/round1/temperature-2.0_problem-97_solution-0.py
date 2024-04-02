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

    r1 = str(a)[-1]
    r2 = str(b)[-1]
    return int(r1) * int(r2)


# print(multiply(148, 412))
# print(multiply(19, 28))
# print(multiply(2020, 1851))
# print(multiply(14, -15))
# print(multiply(0, 0))
# print(multiply(1, 1))
# print(multiply(10, 10))
# print(multiply(100, 100))
# print(multiply(1000, 1000))
# print(multiply(10000, 10000))
# print(multiply(100000, 100000))
# print(multiply(1000000, 1000000))
# print(multiply(10000000, 10000000))
# print(multiply(100000000, 100000000))
# print(multiply(1000000000, 1000000000))
# print(multiply(10000000000, 10000000000))
# print(multiply(100000000000, 100000000000))
# print(multiply(1000000000000, 1000000000000))
# print(multiply(10000000000000, 10000000000000))
# print(multiply(100000000000000, 100000000000000