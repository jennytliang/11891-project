def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: ",
	"""

    mr = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"i":1,"v":5,"x":10
         ,"l":50,"c":100,"d":500,"m":1000}
    r = ''
    rlist = list(reversed([k for k, v in sorted(mr.items(), key=lambda e: e[1]) if v <= number]))
    while number > 0:
        token = rlist.pop(0)
        times = number / mr[token]
        for _ in range(times):
            r += token
            number -= mr[token]
    return r    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
