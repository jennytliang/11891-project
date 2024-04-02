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
    
    m = ["I", "V", "X", "L", "C", "D", "M"]
    n = [1, 5, 10, 50, 100, 500, 1000]
    
    roman = ""
    i = 0
    while number > 0:
        while number < 4:
            roman += m[i]
            number += n[i]
        roman += m[i]
        number -= n[i]
        i += 1
        
    return roman.lower()
