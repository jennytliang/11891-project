def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    return f"db{bin(decimal)[2:]}db"


if __name__ == '__main__':
    print("Example:")
    print(decimal_to_binary(15))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decimal_to_binary(15) == "db1111db", "First"
    assert decimal_to_binary(32) == "db100000db", "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")
