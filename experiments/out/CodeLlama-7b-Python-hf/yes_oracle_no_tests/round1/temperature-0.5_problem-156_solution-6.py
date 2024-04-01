def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code:  m = [" ", "
	Do not include these tokens in the code: roman _ numer als { 1
	"""

    m = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    r = ["", "M", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = []
    i = 0
    while number:
        while number >= 1000:
            res.append(m[i])
            number -= 1000
        while number >= 500:
            res.append(m[i + 1])
            number -= 500
        while number >= 100:
            res.append(m[i + 2])
            number -= 100
        while number >= 50:
            res.append(m[i + 3])
            number -= 50
        while number >= 10:
            res.append(m[i + 4])
            number -= 10
        while number >= 5:
            res.append(m[i + 5])
            number -= 5
        while number >= 4:
            res.append(m[i + 6])
            number -= 4
        while number >= 1:
            res.append(m[i + 7])
            number -= 1
        i += 8
    return "".join(res)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
