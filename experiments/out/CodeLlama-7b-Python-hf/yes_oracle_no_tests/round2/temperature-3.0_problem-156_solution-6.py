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

    m_roman = {1:"i", 4:"iv", 5:"v", 9:"ix", 10:"x", 40:"xl", 50:"l", 90:"xc", 100:"c", 400:"cd", 500:"d", 900:"cm", 1000:"m"}
    
    def int_to_mini_roman(number):
        if number < 1 or number > 1000:
            return 'error'
        roman_num = ''
        for key in sorted(m_roman.keys(), reverse = True):
            if number >= key:
                roman_num += m_roman[key] * int(number / key)
                number = number % key
        return roman_num.lower()
    
    return int_to_mini_roman(number)
    
print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
