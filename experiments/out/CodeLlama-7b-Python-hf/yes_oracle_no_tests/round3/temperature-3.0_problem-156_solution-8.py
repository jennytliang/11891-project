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
    # TODO: Write your solution here
    m = [" ", " m "]
    d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    s = ""
    for i in str(number):
        if int(i) < d[s]:
            s += m[1]
        s += i
    return s.lower()


if __name__=="__main__":
    import doctest
    doctest.testmod()
