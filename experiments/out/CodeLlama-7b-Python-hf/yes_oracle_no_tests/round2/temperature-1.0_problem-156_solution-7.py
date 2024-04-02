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

    #TODO: Use this to develop the full_roman_to_int function!
    """m = ['i','ii','iii','iv','v','vi','vii','viii','ix']
    r = str(num)
    r = r.rjust(3,'0') #fill out the string with '0' so it's full of three digits
    r = r[1:] #get rid of leading "0"
    num_str = ''
    for i in r:
        num_str += m[int(i)] #map i to num_str, convert to string
    return num_str"""
    d = {1:'i', 4:'iv', 5:'v', 9:'ix', 10:'x'}
    q = {1000:'m', 100:'d',  500:'dc', 100:'c', 500:'cc', 10:'x', 50:'l',
         90:'xc', 10:'x', 5:'v', 4:'iv',  1:'i'}
    roman_string = []
    if(number == 0):
        return "0"

    for k,v in d.iteritems():
        if(number >= k):
            roman_string.append((number/k) * v)
            number -= (k*(number/k))
    for k,v in q.iteritems():
        if(number >= k):
            roman_string.append((number/k) * v)
            number -= (k*(number/k))

    return ''.join(roman_string)

def full_roman_to_int(romanString):
    """
    Given a roman numeral, convert it into an integer.
    Restrictions: 1 <= i <= 1000

    Examples:
    >>> full_roman_to_int("III")
    3
    >>> full_roman_to_int("mm")
    2000
    >>> full_roman_to_int("dclxvi")
    666
    