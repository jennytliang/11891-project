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
    i = ['i', 'x', 'c', 'm']
    v = ['v', 'l', 'd']
    r = ['iv', 'ix', 'xc', 'xl', 'xc', 'cd', 'cm']

    def int_to_roman(number):
        if number == 0:
            return ''
        for n in range(len(i)):
            if number == 0:
                return ''
            if number - (5 * n) >= 0:
                return r[n] + int_to_roman(number - (5 * n))
            else:
                return i[n] + int_to_roman(number - (1 * n))

    def roman_to_int(number):
        n = 0
        for i in range(len(number)):
            if number[i] == 'i':
                n += 1
            elif number[i] == 'x':
                n += 5
            elif number[i] == 'c':
                n += 10
            elif number[i] == 'm':
                n += 100
        return n

    def int_to_mini_roman(number):
        roman = int_to_roman(number)
        mini_roman = ''
        for i in range(len(roman)):
            if roman[i] == 'i':
                mini_roman += 'x'
            elif roman[i] == 'x':
                mini_roman += 'l'
            elif roman[i] == 'c':
                mini_roman += 'd'
            else:
                mini_roman += roman[i]
        return mini_roman

    return int_to_mini_roman(number)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
