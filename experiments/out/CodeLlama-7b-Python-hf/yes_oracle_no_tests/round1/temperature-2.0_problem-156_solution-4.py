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
    num = number
    roman = ""
    while num > 0:
        if num % 1000 >= 500:
            roman = roman + "d"
            num = num - 500
        if num % 1000 >= 100:
            roman = roman + "c"
            num = num - 100
        if num % 100 >= 50:
            roman = roman + "l"
            num = num - 50
        if num % 100 >= 10:
            roman = roman + "x"
            num = num - 10
        if num % 10 >= 5:
            roman = roman + "v"
            num = num - 5
        if num % 10 >= 1:
            roman = roman + "i"
            num = num - 1
    return roman.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
