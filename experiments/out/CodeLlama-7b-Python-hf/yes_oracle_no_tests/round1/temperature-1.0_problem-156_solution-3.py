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
    s = ""
    if number // 1000:
        s += m[number // 1000 % 2] + "m "
        number %= 1000
    if number // 500:
        s += m[number // 500 % 2] + "d "
        number %= 500
    if number // 100:
        s += m[number // 100 % 2] + "c "
        number %= 100
    if number // 50:
        s += m[number // 50 % 2] + "l "
        number %= 50
    if number // 10:
        s += m[number // 10 % 2] + "x "
        number %= 10
    if number // 5:
        s += m[number // 5 % 2] + "v "
        number %= 5
    if number:
        s += m[number % 2] + "i "
    return s.strip()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
