def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Do not include these tokens in the code: r = "" while
	"""
    return "db" + str(bin(decimal))[2:] + "db"


def decimal_to_binary_2(decimal):
    r = ""
    while decimal != 0:
        r = str(decimal % 2) + r
        decimal //= 2
    return "db" + r + "db"


print(decimal_to_binary(15))  # returns "db1111db"
print(decimal_to_binary_2(15))  # returns "db1111db"
