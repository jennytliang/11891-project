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
    roman = ""
    roman = roman + m[(number // 1000) % 4] + "m" * (number // 1000)
    roman = roman + m[(number // 100) % 4] + "c" * (number // 100 % 10)
    roman = roman + m[(number // 10) % 4] + "x" * (number // 10 % 10)
    roman = roman + m[(number // 1) % 4] + "i" * (number % 10)
    return roman.replace(" ", "").lower()
