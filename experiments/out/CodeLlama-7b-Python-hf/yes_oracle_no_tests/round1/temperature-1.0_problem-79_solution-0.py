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

    r='{}'.format(bin(decimal))
    return " db" + r[2:][:-1] + "db"

def hex_to_binary(hexadecimal):
    """This function takes a hexadecimal number and returns a string containing that number in
    binary format.  Don't forget to add "db" before and after the binary number for the required
    format.

    Examples:
    hex_to_binary(352)      # returns "db10010011010010db"
    hex_to_binary(2215)     # returns "db1111111000111001db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    ''' r='{}'.format(bin(eval(hex(hexadecimal))))                  # works but does not get rid of "0b"
    return " db" + r[2:][:-1] + "db" '''
    # return " db{}db".format(bin(hexadecimal)[2:][:-1])            # does not get rid of "0b"
    return " db{}db".format(bin((int(hexadecimal, 16)))[2:][:-1])  # works
    
    """
    'hexadecimal' can be converted to binary using 'bin(int(hex(hexadecimal), 16))'
    Then the output is a string of numbers and characters that do not comply with the exercise criteria.
    Therefore, a second conversion step with the slice function is necessary.
    The slice method slices the result generated by the bin function and returns a string with the decimal
    representation of the binary number. Then the conversion to string () is performed to join the string with " db ".
    """

def is_number_binary(number):
    """Returns all the non-binary characters of the number string passed as a parameter.

    Examples:
    is_not_binary('9')                    # returns False
    is_not_binary('1