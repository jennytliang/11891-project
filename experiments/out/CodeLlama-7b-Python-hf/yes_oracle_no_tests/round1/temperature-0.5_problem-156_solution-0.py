def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code:  m = [" ", "
	Do not include these tokens in the code: roman _ numer als { 1
	"""

    # We will be using the roman numeral dictionary
    roman_numerals = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
    }

    # Initialize our string
    roman_numeral = ""

    # Check if the number is in the dictionary
    if number in roman_numerals:
        return roman_numerals[number]

    # If not, then we will need to create the roman numeral
    else:
        # Check if the number is divisible by 1000
        if number % 1000 == 0:
            roman_numeral += roman_numerals[1000]
            number = number - 1000

        # Check if the number is divisible by 900
        if number % 900 == 0:
            roman_numeral += roman_numerals[900]
            number = number - 900

        # Check if the number is divisible by 500
        if number % 500 == 0:
            roman_numeral += roman_numerals[500]
            number = number - 500

        # Check if the number is divisible by 400
        if number % 400 == 0:
            roman_numeral += roman_numerals[400]
            number = number - 400

        # Check if the number is divisible by 100
        if number % 100 == 0:
            roman_numeral += roman_numerals[100]
            number = number - 100

        # Check if the number is divisible by 90
        if number % 90 == 0