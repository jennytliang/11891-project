def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: return " db " + bin
	Do not include these tokens in the code: r =' {} '. format (
	"""

    r = ' db {} '.format(bin(decimal)[2:])

    return r


tests = [
    [32, 'db100000db'],
    [15, 'db1111db'],
    [230, 'db110001101db']
]

for index, test in enumerate(tests):
    out = decimal_to_binary(test[0])
    if out == test[1]:
        print('Test ' + str(index) + ': Pass!')
    else:
        print('Test ' + str(index) + ': FAIL.')
        print('    Your answer was: ' + str(out))