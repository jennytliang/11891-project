def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return "
	Do not include these tokens in the code: ret = '' ret
	"""
    # First, convert the decimal to a binary string
    bin_str = bin(decimal)[2:]
    # Then, add the leading and trailing characters
    return f"db{bin_str}db"


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    num = 32
    print(decimal_to_binary(num))
