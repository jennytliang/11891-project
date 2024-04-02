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

    m = { 1: 'i', 2: 'x', 3: 'c', 4: 'm', 5: 'v', 6: 'l', 7: 'd', 8: 'z', 9: 'y' }
    k = { 10: 'x', 20: 'xx', 30: 'xxx', 40: 'l', 50: 'lx', 60: 'lxx', 70: 'lxxx', 80: 'xcc', 90: 'xc' }
    
    if number < 4:
        return m[number]
    elif number < 9:
        return m[10] * (number % 10)
    elif number < 40:
        t = number // 10
        return k[t * 10] + m[number % 10]
    elif number < 90:
        t = number // 10
        return m[t * 10] + k[(t % 10) * 10]
    elif number < 400:
        t = number // 100
        return m[t * 100] + k[(t % 10) * 100]
    elif number < 900:
        t = number // 100
        return m[t * 100] + k[100] + k[(t % 10) * 100]
    elif number < 4000:
        t = number // 1000
        return m[t * 1000] + k[(t % 10) * 1000]
    elif number < 9000:
        t = number // 1000
        return m[t * 1000] + k[1000] + k[(t % 10) * 1000]
    else:
        return 'out of range'

def test_int_to_mini_roman():
    assert int_to_mini_