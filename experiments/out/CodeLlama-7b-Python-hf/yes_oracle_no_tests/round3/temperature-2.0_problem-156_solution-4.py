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
    roman_numerals = {1:"i", 5:"v", 10:"x", 50:"l", 100:"c", 500:"d", 1000:"m"}
    roman_list = []
    for i in roman_numerals:
        while number >= i:
            roman_list.append(roman_numerals[i])
            number -= i
    return "".join(roman_list).lower().replace(" i ", " i").replace("x i", "xi").replace("c i", "ci")
