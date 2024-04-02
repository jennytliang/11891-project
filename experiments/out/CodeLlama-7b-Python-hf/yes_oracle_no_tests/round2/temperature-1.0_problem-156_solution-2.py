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

    m = {1:"i", 4:"iv", 5:"v", 9:"ix", 10:"x"}
    m.update({11:"xi", 12:"xii", 13:"xiii", 14:"xiv", 15:"xv"})
    m.update({2:"xx", 3:"xxx", 7:"xxvii", 8:"xxviii", 16:"lxxxvi"})
    m.update({30:"xxx", 40:"xl", 50:"l", 90:"xc"})
    m.update({60:"lx", 70:"lxx", 80:"lxxx", 100:"c"})
    m.update({200:"cc", 300:"ccc", 400:"cd", 500:"d", 600:"dc", 700:"dcc", 800:"dcccc", 900:"cm"})
    m.update({1000:"m"})

    ret = []
    for k in sorted(m.keys(), reverse=True):
        while number >= k:
            number -= k
            ret.append(m[k])

    return "".join(ret)
    

def test_int_to_mini_roman():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
