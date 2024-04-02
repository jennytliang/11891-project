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
    # m = ['',' m ']
    mini_roman = int_to_roman(number)
    output = ''
    if len(mini_roman) >= 4:
        mini_roman_start = mini_roman[:4]
        mini_roman_finish = mini_roman[:3] + mini_roman[4:]
    elif len(mini_roman) == 3:
        mini_roman_start = mini_roman[:2] + ' '
        mini_roman_finish = mini_roman[:3]
    else:
        return mini_roman
    for char in mini_roman_start:
        if char == 'I':
            output = output + 'i'
        elif char == ' ':
            output = output
        elif char == 'V':
            output = output + ' ' + 'v'
        else:
            output = output + 'i'
    output = ' '.join(output.split())
    for char in mini_roman_finish:
        if char == 'I':
            output = output + 'i'
        elif char == ' ':
            output = output
        elif char == 'V':
            output = output + ' ' + 'v'
        else:
            output = output + 'i'
    output = ' '.join(output.split())
    return output.lower()


def int_to_roman(number):
    """Return a roman numeral for the given integer."""
    numerals = []
    numerals.append({'value': 1000, 'numeral': 'M'})
    numerals.append({'value': 900, 'numeral': 'CM'})
    numerals.append({'value': 500, 'numeral': 'D'})
    numerals.append({'value': 400, 'numeral': 'CD'})
    numerals.append({'value': 100, 'numeral': 'C'})
    numerals.append({'value': 90, 'numeral': 'XC