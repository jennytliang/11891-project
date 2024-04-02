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
    d = ["", "d", "cd", "ccd", "dd", "cdd", "dcd", "cddd"]
    c = ["", "c", "cc", "ccc", "cd", "cccd", "cdc", "cdcc"]
    x = ["", "x", "xx", "xxx", "xl", "lxx", "lx", "lxxl"]
    v = ["", "v", "vc", "vcc", "vcd", "vccc"]
    u = ["", "u", "uc", "ucc", "ucd", "uccc"]
    t = ["", "t", "tc", "tcc", "tcd", "tcdd", "tdc", "tdcc"]
    
    result = ""
    number = int(number)
    if number >= 1000:
        result += str((number//1000))+"M"
        number = number % 1000
    if number >= 100:
        result += str((number//100))+"C"
        number = number % 100
    if number >= 10:
        result += str((number//10))+"X"
        number = number % 10
    if number >= 1:
        result += str((number))+"I"
    
    return result.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
