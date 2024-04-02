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
    m = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}
    roman_num = ""
    i = 0
    if number <= 0:
    	return "no numbers with negative numbers"
    elif number >= 1000:
    	while number > 1000:
    		roman_num += "M"
    		number -= 1000
    		
    remainder = roman_num
    roman_num = ""
    div = number/100
    if div > 0:
    	i = 0
    	while i < div:
    		roman_num += "C"
    		i += 1
    		
    remainder = roman_num
    number = number%100
    n = str(number)
    roman_num = ""
    if n[0] == 1:
    	roman_num += "X"
    elif n[0] >= 2 and n[0] <= 3:
    	i = 0
    	while i < n[0]:
    		roman_num += "X"
    		i += 1
    elif  n[0] == 4:
    	roman_num += "X"
    	roman_num += "X"
    elif n[0] == 5:
    	roman_num += "L"
    elif n[0] >= 6 and n[0] <= 8:
    	i = 0
    	while i < (n[0]-5):
    		roman_num += "X"
    		i += 1
    		roman_num += "L"
    elif n[0] == 9:
    	roman_num += "X"
    	roman_num += "L"
    if n[1] == 1:
    	roman_num += "I"
    elif n[1] >=