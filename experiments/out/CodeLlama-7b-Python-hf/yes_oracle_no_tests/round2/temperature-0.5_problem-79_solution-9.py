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



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decimal_to_binary(15) == "db1111db", "15"
    assert decimal_to_binary(32) == "db100000db", "32"
    assert decimal_to_binary(9) == "db1001db", "9"
    assert decimal_to_binary(123456789) == "db10110001110101111110110110011db", "123456789"
