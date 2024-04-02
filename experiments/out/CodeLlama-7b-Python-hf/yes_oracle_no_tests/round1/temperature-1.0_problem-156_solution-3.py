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
    m = [" ", " m "] # list of string tokens needed
    d = [1000,900,500,400,100,90,50,40,10,9,5,4,1] # list of integers needed    
    roman_numeral = "" # initialize roman numeral string
    for i in range(len(d)): # use only integer values in list d
        number_temp = number // d[i] # find number temp value equaling num divided by list value
        if number_temp > 0: # if temp value is greater than 0, make room by adding tokens and continue
            roman_numeral = roman_numeral + m[number_temp//10] + m[number_temp%10]
            number = number - number_temp*d[i]
    return roman_numeral 
print(int_to_mini_roman(14))
print(int_to_mini_roman(19))
print(int_to_mini_roman(567))


def mini_roman_to_int(roman):
    """
    Given an input roman numeral string, in lowercase, return its corresponding
    integer value.
    Return -1 for any input that isn't in range (1 <= num <= 1000).
    
    Examples:
    >>> mini_roman_to_int("xix") == 19
    >>> mini_roman_to_int("clii") == 152
    >>> mini_roman_to_int("cdxxvi") == 426
    >>> mini_roman_to_int("mmmm") == -1 # Out of range
    >>> mini_roman_to_int("m") == -1 # Incomplete numeral
    >>> mini_roman_to_int("M") == -1 # Incomplete numeral
    >>> mini_roman_to_int("XL") == -1 # Incomplete numeral
    >>> mini_roman_to_int("XIX") == -1 # Incomplete numeral
   