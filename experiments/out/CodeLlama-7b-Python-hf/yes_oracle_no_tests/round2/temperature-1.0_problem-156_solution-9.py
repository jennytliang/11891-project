def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m
	Do not include these tokens in the code: tokens
	"""


    "*** YOUR CODE HERE ***"
    mini_roman = ''
    tokens = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
          ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
          ('V', 5), ('IV', 4), ('I', 1)]
    for (token, value) in tokens:
        while number >= value:
            number -= value
            mini_roman += token

    return mini_roman
    

#print(int_to_mini_roman(1))

def mini_roman_to_int(mini_roman):
    """
    Given a roman numeral as a lowercase string, return an integer
    representing its decimal value.
    Restrictions: len(mini_roman) <= 14, roman numerals are well-formed

    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
    
	Include these tokens in the code: m
	Do not include these tokens in the code: tokens
    """


    "*** YOUR CODE HERE ***"

    tokens = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
              ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
              ('V', 5), ('IV', 4), ('I', 1)]

    for (token, value) in tokens:
        mini_roman = mini_roman.replace(token, str(value))
    return