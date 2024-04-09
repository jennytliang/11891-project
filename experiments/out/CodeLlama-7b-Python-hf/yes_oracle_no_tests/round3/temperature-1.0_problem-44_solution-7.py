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
        return "2"
    if x == 3:
        return "3"
    if x == 4:
        return "4"
    if x == 5:
        return "5"
    if x == 6:
        return "6"
    if x == 7:
        return "7"
    if x == 8:
        return "8"
    if x == 9:
        return "9"

    num = ""
    while x > 0:
        num = change_base(x % base, base) + num
        x = x // base
    return num


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
        return "2"
    if x == 3:
        return "3"
    if x == 4:
        return "4"
    if x == 5:
        return "5"
    if x == 6:
        return "6"
    if x == 7:
        return "7"
    if x == 8:
        return "8"
    if x == 9:
        return "9"

    num = ""
    while x > 0:
        num = change_base(x % base, base) + num
        x = x // base
    return num



if __name__ ==