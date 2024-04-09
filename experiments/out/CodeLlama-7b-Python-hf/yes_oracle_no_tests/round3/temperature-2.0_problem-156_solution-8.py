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

    # Create a list of roman numeral equivalents for numbers 1-10
    m = ["I", "X", "C", "M"]

    # Initialize the final_roman_numeral string to an empty string
    final_roman_numeral = ""

    # While number is greater than 0
    while number > 0:
        # If number is divisible by 10, add a 'X' to the final_roman_numeral string
        if number >= 10:
            final_roman_numeral += "X"
            number -= 10
        # If number is divisible by 5, add a 'V' to the final_roman_numeral string
        elif number >= 5:
            final_roman_numeral += "V"
            number -= 5
        # If number is divisible by 4, add a 'I' to the final_roman_numeral string
        elif number >= 4:
            final_roman_numeral += "I"
            number -= 4
        # If number is divisible by 3, add 'III' to the final_roman_numeral string
        elif number >= 3:
            final_roman_numeral += "III"
            number -= 3
        # If number is divisible by 2, add 'II' to the final_roman_numeral string
        elif number >= 2:
            final_roman_numeral += "II"
            number -= 2
        # If number is divisible by 1, add 'I' to the final_roman_numeral string
        elif number >= 1:
            final_roman_numeral += "I"
            number -= 1

    # Return the final_roman_numeral string in lowercase
    return final_roman_numeral.lower()


def main():
    import doctest
    doctest.testmod()
    print(int_to_mini_roman(19))
    print(int_to_mini_roman(152))
    print(int_to