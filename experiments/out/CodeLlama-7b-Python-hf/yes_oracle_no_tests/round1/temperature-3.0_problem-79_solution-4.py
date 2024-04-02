def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f '
	"""

    r = "db"
    while decimal > 0:
        r = str(decimal % 2) + r
        decimal = decimal // 2
    r = "db" + r + "db"
    return r


def decimal_to_binary_2(decimal):
    # return "db" + "".join(map(str, [int(d) for d in str(bin(decimal))[2:]])) + "db"
    return "db" + str(bin(decimal))[2:] + "db"


def decimal_to_binary_3(decimal):
    r = []
    while decimal > 0:
        r.append(str(decimal % 2))
        decimal = decimal // 2
    return "db" + "".join(r[::-1]) + "db"


def decimal_to_binary_4(decimal):
    return "db" + "".join(map(lambda x: str(x), [int(d) for d in str(bin(decimal))[2:]])) + "db"


if __name__ == '__main__':
    assert decimal_to_binary(15) == "db1111db", decimal_to_binary(15)
    assert decimal_to_binary(32) == "db100000db", decimal_to_binary(32)
    assert decimal_to_binary_2(15) == "db1111db", decimal_to_binary_2(15)
    assert decimal_to_binary_2(32) == "db100000db", decimal_to_binary_2(32)
    assert decimal_to_binary_3(15) == "db1111db", decimal_to_binary_3(15)
    assert decimal_to_binary_3(32) == "db100000db", decimal_to_binary_3(32)
    assert decimal_to_binary_4(15) == "db1111db", decimal_to_binary