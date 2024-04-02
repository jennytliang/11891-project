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

    # Divide number by 10 and obtain quotient and remainder
    quotient, remainder = divmod(number, 10)

    # Recursive call
    roman_number = int_to_mini_roman(quotient)

    if remainder == 1:
        roman_number += "i"
    elif remainder == 2:
        roman_number += "ii"
    elif remainder == 3:
        roman_number += "iii"
    elif remainder == 4:
        roman_number += "iv"
    elif remainder == 5:
        roman_number += "v"
    elif remainder == 6:
        roman_number += "vi"
    elif remainder == 7:
        roman_number += "vii"
    elif remainder == 8:
        roman_number += "viii"
    elif remainder == 9:
        roman_number += "ix"
    else:
        roman_number += "x"

    return roman_number


if __name__ == "__main__":
    import doctest
    doctest.testmod()
