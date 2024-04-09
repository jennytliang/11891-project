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
    roman_numerals = [
        (1000, "m"),
        (500, "d"),
        (100, "c"),
        (50, "l"),
        (10, "x"),
        (5, "v"),
        (1, "i"),
    ]
    roman = ""
    for (numeral, letter) in roman_numerals:
        while number >= numeral:
            roman += letter
            number -= numeral
    return roman.lower()


# 	Another implementation
# 	def int_to_mini_roman(number):
# 		"""
# 		Given a positive integer, obtain its roman numeral equivalent as a string,
# 		and return it in lowercase.
# 		Restrictions: 1 <= num <= 1000

# 		Examples:
# 		>>> int_to_mini_roman(19) == 'xix'
# 		>>> int_to_mini_roman(152) == 'clii'
# 		>>> int_to_mini_roman(426) == 'cdxxvi'

# 		Include these tokens in the code: m = [" ", " m "]
# 		"""
# 		m = [" ", " m "]
# 		roman_numerals = [
# 			(1000, "m"),
# 			(500, "d"),
# 			(100, "c"),
# 			(50, "l"),
# 			(10, "x"),
# 			(5, "v"),
# 			(1, "i"),
# 		]
# 		roman = ""
# 		for (numeral, letter) in roman_numerals:
# 			while number >= numeral:
# 			