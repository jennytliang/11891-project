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

    m_roman = {1:'i', 5:'v', 10:'x', 50:'l', 100:'c', 500:'d', 1000:'m'}
    r_roman = ['','i','ii','iii','iv','v','vi','vii','viii','ix']
    r_roman.reverse()
    r_roman_10 = ['','x','xx','xxx','l','lx','lxx','lxxx','xl','xc']
    r_roman_10.reverse()
    r_roman_100 = ['','c','cc','ccc','cd','d','dd','ddd','dm','cm']
    r_roman_100.reverse()
    r_roman_1000 = ['','m','mm','mmm']
    r_roman_1000.reverse()

    def int_to_mini_roman(number):
        if number < 1 or number > 5000:
            return 'Input number out of range.'
        if number == 0:
            return ''
        if number < 5:
            return r_roman[number]
        if number < 10:
            return m_roman[5] + r_roman[number - 5]
        if number < 50:
            return m_roman[5] + r_roman[number - 10]
        if number < 100:
            return m_roman[10] + r_roman[number - 50]
        if number < 500:
            return m_roman[50] + r_roman[number - 100]
        if number < 1000:
            return m_roman[100] + r_roman[number - 500]
        if number < 5000:
            return m_roman[500] + r_roman[number - 1000]
        
    def int_to_mini_roman(number