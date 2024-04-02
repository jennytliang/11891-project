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

    r =''
    x = 'db'
    y= int(decimal)
    print (y)

    while y+1 > 0:
        if (y % 2) > 0:
            r = r +'1'
        else:
            r = r + '0'
        y = y // 2
        print(y)
    print(r[::-1])
    return x + r[::-1] + x

