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
    # TODO: write your code here
    m = [" ", " m "]
    roman_dictionary = {1000: " m", 900: " cm", 500: " d", 400: " cd", 100: " c", 90: " xc", 50: " l", 40: " xl", 10: " x ", 9: " ix", 5: " v", 4: " iv", 1: " i"}
    res = ""
    for i in roman_dictionary.keys():
        while number >= i:
            res += roman_dictionary[i]
            number -= i
    return res.lower()

print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))