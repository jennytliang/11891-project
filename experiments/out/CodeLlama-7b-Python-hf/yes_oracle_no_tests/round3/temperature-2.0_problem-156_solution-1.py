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
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def int_to_roman(number):
        number = int(number)
        if number == 0:
            return ""
        for i in d:
            while d[i] <= number:
                number -= d[i]
                yield i

    def roman_to_mini_roman(roman):
        roman = roman.upper()
        return roman[0] + "".join("I" if r == "X" else r for r in roman)

    return "".join(map(roman_to_mini_roman, int_to_roman(number)))


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    m = [" ", " m "]
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def int_to_roman(number):
        number = int(number)
        if number == 0:
            return ""
        for i in d:
            while d[i] <= number:
                number -= d[i]
                yield i

    return "".join(int_to_roman(number))


def