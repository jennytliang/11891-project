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
    digits = [int(digit) for digit in list(str(x))]
    return_string = ''
    is_base2 = True
    if(x == 0):
        # For the purpose of consistency of returning string, I add a space for the 0.
        return '0 '
        return False

    while(x >= base and is_base2 is True):  # for base=2 we check whether x>=2 or x<2 and return a string of 1's or 0s accordingly
        
