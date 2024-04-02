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
    tokens = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    tokens2 = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C"]
    tokens3 = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]
    m = [" ", " m "]
    
    number_list = []
    
    while number >= 1000 : # add 1000's to number_list
        tens = number // 1000
        number = number % 1000
        number_list.append(tokens3[tens-1])
    
    while number >= 100 : # add 100's to number_list
        tens = number // 100
        number = number % 100
        number_list.append(tokens2[tens-1])

    if number >= 10 : # add 10 to 19 if 10 <= number <= 19
        ones = number // 10
        number_list.append(tokens[ones-1])
        
    elif number == 9 :  # add nine if number == 9
        number_list.append('ix')

    elif number == 8 : # add eight if number == 8
        number_list.append('viii')
        
    elif number == 7 :  # add seven if number == 7
        number_list.append('vii')

    elif number == 6 :  # add six if number == 6
        number_list.append('vi')
        
    elif number == 5 : # add five if number == 5
        number_list.append('v')
        
    elif number == 4 : # add four if number == 4
        number_list.append('iii')
        
    elif number == 3 : # add three if number == 