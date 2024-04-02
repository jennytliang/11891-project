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

    m = [" I", "V", " X", "L", "C", "D", " M"]
    n = [1000, 500, 100, 50, 10, 5, 1]
    
    # Initialize roman string
    roman = ""
    
    # Loop through each of the numbers
    for i in range(len(n)):
        while number >= n[i]:
            roman += m[i]
            number -= n[i]

    return roman.lower()


# Pybites solution

def int_to_mini_roman1(number):
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

    m = [" I", "V", " X", "L", "C", "D", " M"]
    n = [1000, 500, 100, 50, 10, 5, 1]

    roman = ""

    for i in range(len(n)):
        while number >= n[i]:
            roman += m[i]
            number -= n[i]

    return roman.lower()
