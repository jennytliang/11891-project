def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: db "
	"""

    ret = []
    ret.append("db")
    ret.append("1" * 5)

    for i in range(10):
        ret.append("1" if decimal % 2 == 1 else "0")
        decimal = decimal // 2
    ret.append("db")
    return "".join(ret)


def decimal_to_binary_v2(decimal):
    return "db" + "1" * 5 + "".join(
        "1" if decimal % 2 == 1 else "0" for decimal in range(10)
    ) + "db"


print(decimal_to_binary(15))
print(decimal_to_binary_v2(15))
