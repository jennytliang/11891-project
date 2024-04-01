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

    string = ''
    for name in 'm', 'c', 'x':
        if number >= len(name):
            number, index = len(name), string.index(name)
            string = ''
            string += string[: index] + name
        else:
            pass
    for digit, name, place, small_roman in (
        ((number - (len('c') + len('i') ) ), 'c', 'vii', 'ix'),
        (len(string) == len('x') + len('i'), 'm', 'iii', 'iv')
            ): string += string * place + name*number