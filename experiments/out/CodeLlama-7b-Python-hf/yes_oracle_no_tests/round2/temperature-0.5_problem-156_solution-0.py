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

    # Define the tokens
    tokens = [
        " ",
        " m ",
        " d ",
        " c ",
        " l ",
        " x ",
        " v ",
        " u ",
        " n ",
        " p ",
        " b ",
        " z ",
    ]

    # Define the values of the tokens
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Create an empty string to store the roman numeral
    roman_numeral = ""

    # Loop through the tokens and values
    for token, value in zip(tokens, values):

        # If the number is greater than the value, append the token to the roman numeral
        if number >= value:
            roman_numeral += token
            number -= value

    # Return the roman numeral
    return roman_numeral.lower()
