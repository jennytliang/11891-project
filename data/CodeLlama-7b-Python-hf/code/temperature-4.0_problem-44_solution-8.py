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

    if x<0 or base<=0:
        raise Exception("base needs to be base numbers are "
                        "great than zero and the value must be a non-negative integer.")

    if x//base != 0:  # x//base always >= 0.
        raise Exception("this is the example for this method. "
                          "you need to implement the core logic first")
    r=""
    