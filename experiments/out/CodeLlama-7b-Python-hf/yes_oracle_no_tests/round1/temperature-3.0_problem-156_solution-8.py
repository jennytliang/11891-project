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

    m = [" ", " m "]

    # Dictionary for the conversion
    d = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }

    # Converts the number to a string
    number = str(number)

    # Checks if the number is valid
    if len(number) > 3 or int(number) > 3999 or int(number) < 1:
        raise ValueError("Invalid number")

    # Creates the roman number
    roman_number = ""

    # Checks if the number is a single digit
    if len(number) == 1:
        roman_number = d[int(number)]

    # Checks if the number is a double digit
    elif len(number) == 2:
        roman_number = d[int(number[0] * 10)] + d[int(number[1])]

    # Checks if the number is a triple digit
    elif len(number) == 3:
        roman_number = d[int(number[0] * 100)] + d[int(number[1] * 10)] + d[int(number[2])]

    # Returns the roman number
    return roman_number.lower()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
