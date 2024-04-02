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

    r = ''
    while decimal != 0:
        r = '0' + r if not decimal % 2 else '1' + r
        decimal = decimal // 2
    return "db" + r + "db"


print(decimal_to_binary(15))
print(decimal_to_binary(32))
print(decimal_to_binary(48))
print(my_func(15))
print(my_func(32))
print(my_func(48))


# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com


def decimal_to_binary(decimal):
  return "db" + (str(bin(decimal)[2:])) + "db"


decimal_to_binary(15)
decimal_to_binary(32)
decimal_to_binary(48)
