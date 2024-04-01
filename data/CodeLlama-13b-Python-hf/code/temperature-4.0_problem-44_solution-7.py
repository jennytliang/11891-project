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
    if (not isinstance(x, (int, list)) or not (base < 10)):
        raise TypeError('The function change_base() just accepts integer input \
                        with base less thatn than 10. ')
