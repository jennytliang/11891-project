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
    
	Include these tokens in the code: ret
	Do not include these tokens in the code: # change the base of x to base
	"""


    if x == 0:
 
       return '0'

    if x < 0:
       return '-' + change_base(-x, base)

    digits = []

    while x > 0:
       digits.append(str(x % base))
       x = x // base

    return ''.join(digits)


