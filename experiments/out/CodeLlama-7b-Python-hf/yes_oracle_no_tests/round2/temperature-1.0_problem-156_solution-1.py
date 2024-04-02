def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: # Write your code here
	"""

    roman = ''
    
    number = int(number)
    while number >= 1000:
        roman += 'm'
        number -= 1000
        
    if number >= 900:
        roman += 'cm'
        number -= 900
        
    if number >= 800:
        roman += 'dccl'
        number -= 800
        
    if number >= 700:
        roman += 'dcc'
        number -= 700
        
    if number >= 600:
        roman += 'dc'
        number -= 600
        
    if number >= 500:
        roman += 'd'
        number -= 500
    
    if number >= 400:
        roman += 'cd'
        number -= 400
        
    if number >= 300:
        roman += 'ccc'
        number -= 300
        
    if number >= 200:
        roman += 'cc'
        number -= 200
        
    if number >= 100:
        roman += 'xc'
        number -= 100
        
    if number >= 90:
        roman += 'xl'
        number -= 90
        
    if number >= 80:
        roman += 'lxxx'
        number -= 80
        
    if number >= 70:
        roman += 'lxx'
        number -= 70
        
    if number >= 60:
        roman += 'lx'
        number -= 60
        
    if number >= 50:
        roman += 'l'
        number -= 50
        
    if number >= 40:
        roman += 'xx'
        number -= 40
        
    if number >= 30:
        roman += 'xx'
        number -= 30
        
    if number >= 20:
        roman += 'x'
        number -= 20
        
    if number >= 1