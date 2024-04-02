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
    
    conversion = {1:"i", 5:"v", 10:"x", 50:"l", 100:"c", 500:"d", 1000:"M"}
    m = [" ", " m "] 
    k = 1
    mini_roman_numeral = ""

    while number > 0:

        #Check which key the number is equat to
        
        for i in conversion:
            if  number == i:
                mini_roman_numeral += conversion[i]
                number -= i
                break

        #For all numbers less than 1000
        elif number > 1: 
            while number >= k:
                if k == 1:
                    mini_roman_numeral += 'i '
                if k > 1 and k < 4:
                    mini_roman_numeral += m[-1]*(k-1)
                    mini_roman_numeral += 'i'
                if k < number:
                    mini_roman_numeral += m[-2]
                if number % k != 0:
                    n = (number % k)

                number //= k
                k *= 5

    return mini_roman_numeral.strip()