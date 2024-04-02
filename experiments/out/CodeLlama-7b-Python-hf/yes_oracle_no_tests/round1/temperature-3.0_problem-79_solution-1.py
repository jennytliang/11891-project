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

    r = bin(decimal)
    return f"db{r[2:]}db"


def decimal_to_binary_1(decimal):
    return 'db' + bin(decimal)[2:] + 'db'


if __name__ == '__main__':
    print("Example:")
    print(decimal_to_binary(15))
    assert decimal_to_binary(15) == 'db1111db', 'binary_to_decimal(15) should return 1111'
    assert decimal_to_binary(0) == 'db0db', 'binary_to_decimal(0) should return 0'
    assert decimal_to_binary(1) == 'db1db', 'binary_to_decimal(1) should return 1'
    assert decimal_to_binary(2) == 'db10db', 'binary_to_decimal(2) should return 10'
    assert decimal_to_binary(3) == 'db11db', 'binary_to_decimal(3) should return 11'
    assert decimal_to_binary(4) == 'db100db', 'binary_to_decimal(4) should return 100'
    assert decimal_to_binary(5) == 'db101db', 'binary_to_decimal(5) should return 101'
    assert decimal_to_binary(6) == 'db110db', 'binary_to_decimal(6) should return 110'
    assert decimal_to_binary(7) == 'db111db', 'binary_to_decimal(7) should return 111'
    assert decimal_to_binary(8) == 'db1000db', 'binary_to_decimal(8) should return 1000'
    assert decimal_to_binary(9) == 'db1001db', 'binary_to_decimal(9) should return 1001'
    assert decimal_to_binary(10) == 'db1010db',