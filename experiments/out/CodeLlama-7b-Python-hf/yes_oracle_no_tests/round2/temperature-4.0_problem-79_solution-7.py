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

    ret = 'db'
    while decimal > 0:
        ret = str(decimal % 2) + ret
        decimal = decimal // 2
    ret = 'db' + ret + 'db'
    return ret


def decimal_to_binary(decimal):
    return 'db' + bin(decimal)[2:] + 'db'


if __name__ == '__main__':
    print("Example:")
    print(decimal_to_binary(15))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(999) == "db1111111111111001db"
    assert decimal_to_binary(1234567890) == "db100111101001000101001000000000010db"
    print("Coding complete? Click 'Check' to earn cool rewards!")
