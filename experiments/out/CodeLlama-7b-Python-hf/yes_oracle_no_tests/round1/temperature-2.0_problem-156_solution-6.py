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
    m = ["I","II","III","IV","V","VI","VII","VIII","IX"]
    r = []
    if number < 1 or number > 1000:
        raise ValueError("Input out of range: 1 <= number <= 1000")
    while number > 0:
        r.append(m[number%10])
        number = number//10
    return "".join(r)

if __name__ == "__main__":
    import doctest
    doctest.testmod()