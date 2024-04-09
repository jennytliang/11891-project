def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: = {" I ": 1 , " V ":
	"""

    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_numerals_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def roman_from_int(number):
        roman_number = ''
        for i in range(len(roman_numerals_list)):
            while number >= roman_numerals[roman_numerals_list[i]]:
                roman_number += roman_numerals_list[i]
                number -= roman_numerals[roman_numerals_list[i]]
        return roman_number

    def int_from_roman(roman_number):
        roman_numerals_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_numerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        for i in range(len(roman_numerals_list)):
            if roman_number.startswith(roman_numerals_list[i]):
                return roman_numerals[roman_numerals_list[i]] + int_from_roman(roman_number[len(roman_numerals_list[i]):])
        return 0

    if number <= 0:
        raise ValueError('Please provide a positive integer')
    elif number > 1000:
        raise ValueError('Please provide