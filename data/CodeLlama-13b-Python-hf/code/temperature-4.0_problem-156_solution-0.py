def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    numeral_symbol_dict = {"1": "i", "4": "iv", "5": "v",
                           "9": "ix", "10": "x", "40": "xl",
                           "50": "l", "90": "xc", "100": "c",
                           "400": "cd", "500": "d", "900": "cm",
                           "1000": "m"}
    output = []  # we want to return this value

    # 2-9 are too complicated to represent with
    # numeral, so convert them as is (in string format) to add them to output
    while number >= 10:
        number_string = str(number)
        for idx, number_digit in enumerate(number_string):
            output += [numeral_symbol_dict[number_digit]]
        break  # no more processing if number is more than hundreds of thousands

    # number_string = '152'.  Now we need to process each digit. '1' -> 'i' -> 'i'
    for char in number_string[1:]:
        output += numeral_symbol_dict[char]
