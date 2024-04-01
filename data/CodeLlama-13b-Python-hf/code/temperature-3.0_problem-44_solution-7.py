def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    if x == 0:
        return '0'
    if x < 0:
        sign = '-'
        x *= -1
    else:
        sign = ''

    output = ''
    y = 0
    while x > 0:
        y = x % base
        output += str(y)
        x = x // base

    output = output[::-1]
    return sign+output