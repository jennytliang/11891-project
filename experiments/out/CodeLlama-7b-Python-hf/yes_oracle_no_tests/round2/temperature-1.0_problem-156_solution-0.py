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
    numbers = [
        ("c", 100),
        ("cx", 90),
        ("xc", 90),
        ("l", 50),
        ("lx", 40),
        ("xl",  40),
        ("x", 10),
        ("ix", 9),
        ("v", 5),
        ("vi", 4),
        ("iv", 4),
        ("i", 1)
    ]
    string = ""
    for i in numbers:
        if number >= i[1]:
            rep = int(number/i[1])
            string += rep * i[0]
            number %= i[1]
    return string

#Tests

def test_int_to_mini_roman():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

if __name__ == '__main__':
    test_int_to_mini_roman()
