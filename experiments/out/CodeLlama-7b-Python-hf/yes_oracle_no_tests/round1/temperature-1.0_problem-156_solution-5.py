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
    for i in range(len(m)):
        while number > 1000:
            number -= 1000
            roman += 'm' + m[i]
        while number > 500:
            number -= 500
            roman += 'd' + m[i]
        while number > 100:
            number -= 100
            roman += 'c' + m[i]
        while number > 50:
            number -= 50
            roman += 'l' + m[i]
        while number > 10:
            number -= 10
            roman += 'x' + m[i]
        while number > 5:
            number -= 5
            roman += 'v' + m[i]
        while number > 1:
            number -= 1
            roman += 'i' + m[i]
    return roman

if __name__ == '__main__':
    import doctest
    doctest.testmod()
