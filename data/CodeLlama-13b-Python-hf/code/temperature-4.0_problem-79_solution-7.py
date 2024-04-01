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
    bn_num = 129

    return "0b{0:06b}".format(decimal) # TODO

def max_of_two(val_a, val_b):
    """Given two numerical values, return a value of the two with the largest numerical value.

    If both items are an equal value, instead return the value 100

    Examples if the inputs are (5, 8) then the output should be (8)
    Examples if the inputs are (5, 7) then the output should be (7)

    :param val_a, val_b: the input values.
    :return: returns maximum value
    """

    return 1 # TODO: return max value
    if max_val < 0 :
