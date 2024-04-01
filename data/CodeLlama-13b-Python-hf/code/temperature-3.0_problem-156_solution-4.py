def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    
    thousands = ['', 'm', 'mm', 'mmm']
    hundreds = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']
    tens = ['', 'x', 'xx', 'xxx', 'l', 'lx', 'lxx', 'lxxx', 'xc', 'xl', 'l', 'xc', 'l', 'xc', 'l', 'xc', 'l']
    ones = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    
    result = thousands[number // 1000] + hundreds[(number % 1000) // 100] + tens[(number % 100) // 10] + ones[number % 10]
    return result