def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    # Base case
    if number == 0:
        return ""
    # Recursive case
    else:
        # Add the last token based on the number
        if number == 1:
            return "i"
        elif number == 2:
            return "ii"
        elif number == 3:
            return "iii"
        elif number == 4:
            return "iv"
        elif number == 5:
            return "v"
        elif number == 6:
            return "vi"
        elif number == 7:
            return "vii"
        elif number == 8:
            return "viii"
        elif number == 9:
            return "ix"
        elif number == 10:
            return "x"
        elif number == 11:
            return "xi"
        elif number == 12:
            return "xii"
        elif number == 13:
            return "xiii"
        elif number == 14:
            return "xiv"
        elif number == 15:
            return "xv"
        elif number == 16:
            return "xvi"
        elif number == 17:
            return "xvii"
        elif number == 18:
            return "xviii"
        elif number == 19:
            return "xix"
        elif number == 20:
            return "xx"
        elif number == 30:
            return "xxx"
        elif number == 40:
            return "xl"
        elif number == 50:
            return "l"
        elif number == 60:
            return "lx"
        elif number == 70:
            return "lxx"
        elif number == 80:
            return "lxxx"
        elif number == 90:
            return "xc"
        elif number == 100:
            return "c"
        elif number == 200:
            return "cc"
        elif number == 300:
            return "ccc"
        elif number ==