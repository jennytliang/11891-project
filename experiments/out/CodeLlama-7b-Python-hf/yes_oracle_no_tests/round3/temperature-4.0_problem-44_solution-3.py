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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 1
    def convert_to_base(x, base):
        if x == 0:
            return "0"
        if x < 0:
            return "-" + convert_to_base(-x, base)

        digits = []
        while x:
            digits.append(str(x % base))
            x //= base
        return "".join(digits[::-1])

    return convert_to_base(x, base)
    # END PROBLEM 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()