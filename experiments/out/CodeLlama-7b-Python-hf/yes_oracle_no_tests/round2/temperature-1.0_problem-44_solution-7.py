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
    
	Include these tokens in the code: "
	Do not include these tokens in the code: '
	"""


    if x == 0:
        return 0
    if x < 10:
        return x
    if x > base**10:
        raise ValueError("Input number is too large")
    n = len(str(x))
    base_list = []
    for i in range(n):
        remainders = x % base
        base_list.append(remainders)
        x = int((x - remainders) / base)
    return ''.join([str(num) for num in base_list][::-1])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
