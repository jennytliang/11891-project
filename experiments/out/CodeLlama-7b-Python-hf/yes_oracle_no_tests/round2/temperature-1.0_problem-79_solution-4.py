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
	Do not include these tokens in the code: r = '' x
	"""
    return 'db' + 'r'.join(bin(decimal)[2:]) + 'db'

if __name__ == '__main__':
    # Do not remove the `if __name__ == "__main__"` construct
    # and below when copying in and running this code.
    userInput = int(input('Enter a Decimal Value: '))
    print(decimal_to_binary(userInput))
