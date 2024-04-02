def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    r = ''
    for i in range(15):
        r += '0' if decimal & 1 else '1'
        decimal >>= 1
    return 'db' + r[::-1] + 'db'


assert decimal_to_binary(15) == "db1111db", "Error: " + decimal_to_binary(15)
assert decimal_to_binary(32) == "db100000db", "Error: " + decimal_to_binary(32)

print("Testing code: OK")
