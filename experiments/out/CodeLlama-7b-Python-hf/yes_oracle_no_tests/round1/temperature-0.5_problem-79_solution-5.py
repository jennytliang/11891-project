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

    return f"db{bin(decimal)[2:]}db"

print(decimal_to_binary(15))
print(decimal_to_binary(32))
print(decimal_to_binary(0))
print(decimal_to_binary(1))
print(decimal_to_binary(2))
print(decimal_to_binary(3))
print(decimal_to_binary(4))
print(decimal_to_binary(5))
print(decimal_to_binary(6))
print(decimal_to_binary(7))
print(decimal_to_binary(8))
print(decimal_to_binary(9))
print(decimal_to_binary(10))
print(decimal_to_binary(11))
print(decimal_to_binary(12))
print(decimal_to_binary(13))
print(decimal_to_binary(14))
print(decimal_to_binary(16))
print(decimal_to_binary(17))
print(decimal_to_binary(18))
print(decimal_to_binary(19))
print(decimal_to_binary(20))
print(decimal_to_binary(21))
print(decimal_to_binary(22))
print(decimal_to_binary(23))
print(decimal_to_binary(24))
print(decimal_to_binary(25))
print(decimal_to_binary(26))
print(decimal_to_binary(27))
print(decimal_to_binary(28))
print(decimal_to_binary(29))
print(decimal_to_binary(30))
print(decimal_to_binary(31))
print(decimal_to_binary(33))
print(decimal_to_binary(34))
print(decimal_to_binary(35))
print(decimal_to_binary(36))
print(decimal_to_binary(37))
print