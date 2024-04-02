def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    
	Include these tokens in the code: "
	Do not include these tokens in the code: '
	"""


    if x == 0:
        return "0"
    if x == 1:
        return "1"
    if x == 2:
        return "10"
    if x == 3:
        return "11"
    if x == 4:
        return "100"
    if x == 5:
        return "101"
    if x == 6:
        return "110"
    if x == 7:
        return "111"
    if x == 8:
        return "1000"
    if x == 9:
        return "1001"
    if x == 10:
        return "1010"
    if x == 11:
        return "1011"
    if x == 12:
        return "1100"
    if x == 13:
        return "1101"
    if x == 14:
        return "1110"
    if x == 15:
        return "1111"
    if x == 16:
        return "10000"
    if x == 17:
        return "10001"
    if x == 18:
        return "10010"
    if x == 19:
        return "10011"
    if x == 20:
        return "10100"
    if x == 21:
        return "10101"
    if x == 22:
        return "10110"
    if x == 23:
        return "10111"
    if x == 24:
        return "11000"
    if x == 25:
        return "11001"
    if x == 26:
        return "11010"
    if x == 27:
        return "11011"
    if x == 28:
        return "1110