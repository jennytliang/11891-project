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
    # YOUR CODE HERE
    m = [" ", " m "]
    roman_numerals = {
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

    # create a list of roman numeral tokens
    roman_numeral_tokens = []
    for key in roman_numerals.keys():
        roman_numeral_tokens.append(roman_numerals[key])

    # create a dictionary of roman numeral tokens
    roman_numeral_tokens_dict = {}
    for i in range(len(roman_numeral_tokens)):
        roman_numeral_tokens_dict[roman_numeral_tokens[i]] = i

    # initialize the result string
    result = ""

    # loop over the tokens, adding them to the result string
    for i in range(len(roman_numeral_tokens)):
        while number >= 10 ** (len(roman_numeral_tokens) - i - 1):
            number -= 10 ** (len(roman_numeral_tokens) - i - 1)
            result += roman_numeral_tokens[i]

    return result.lower()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
