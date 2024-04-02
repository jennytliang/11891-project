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
    
	Include these tokens in the code: return
	"""


    if x <= 9 and x >= 0:
        return str(x)
    else:

        result_list = []
        while x != 0:
            remainder = x % base
            result_list.insert(0, str(remainder))
            x = x - remainder
            x = x // base

        return "".join(result_list)
