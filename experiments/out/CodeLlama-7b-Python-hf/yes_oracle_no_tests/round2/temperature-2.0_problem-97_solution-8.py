def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Do not include these tokens in the code: r = str ( a )
	"""

    # Split the numbers into their individual digits
    a_digits = [int(digit) for digit in str(a)]
    b_digits = [int(digit) for digit in str(b)]

    # Multiply each digit in a by each digit in b
    product = [a_digit * b_digit for a_digit in a_digits for b_digit in b_digits]

    # Return the sum of the product
    return sum(product)

print(multiply(148, 412)) # Should print 16
print(multiply(19, 28)) # Should print 72
print(multiply(2020, 1851)) # Should print 0
print(multiply(14, -15)) # Should print 20