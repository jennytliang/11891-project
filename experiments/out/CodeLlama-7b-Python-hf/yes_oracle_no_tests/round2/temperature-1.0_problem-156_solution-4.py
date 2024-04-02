def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: I
	"""


    
int_to_mini_roman(19) + int_to_mini_roman(152) + int_to_mini_roman(426)


    """
    roman_lookup = [
        ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'],
        ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc'],
        ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm'],
        ['', 'm', 'mm', 'mmm']]
    for digit in str(number):
        index = int(digit) if (int(digit) < 10) else 9
        print(roman_lookup[3].pop(index) * digit)

    print(roman_lookup[3])
    
    
    
    print("roman lookup 3 ",roman_lookup[3][len(roman_lookup[3])-1])
    print(roman_lookup[3].pop(len(roman_lookup[3])-1))

"""