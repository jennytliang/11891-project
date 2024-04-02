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
    n = ["i", "x", "c", "m"]
    r = ""
    i = 0
    while number > 0:
        if number % 1000 > 0:
            r = m[int(number % 1000 / 1000)] + r
            number = number % 1000
        else:
            number = number - number % 1000
        if number % 100 > 0:
            if number % 100 < 4:
                r = n[int(number % 100 / 10)] + r
            elif number % 100 == 4:
                r = n[2] + n[int(number % 100 / 10)] + r
            elif number % 100 == 5:
                r = n[4] + r
            elif number % 100 > 5 and number % 100 < 9:
                r = n[int(number % 100 / 10)] + n[int(number % 10 / 10)] + r
            elif number % 100 == 9:
                r = n[n[int(number % 100 / 10)]] + n[2] + r
            number = number - number % 100
        else:
            number = number - number % 100
        if number % 10 > 0:
            if number % 10 < 4:
                r = n[int(number % 10 / 10)] + r
            elif number % 10 == 4:
                r = n[2] + n[int(number % 10 / 10)] + r
            elif number % 10 == 5:
                r = n[4] + r
            elif number % 10 > 5 and number % 10 < 9:
                r = n[int(number % 10 / 10)] + n[int(number % 10