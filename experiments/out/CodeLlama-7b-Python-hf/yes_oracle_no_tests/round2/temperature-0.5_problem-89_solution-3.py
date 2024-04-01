def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    # Initialize a dictionary with the letters of the alphabet as keys
    # and the letters they should be shifted to as values.
    shift = {'a':'c', 'b':'d', 'c':'e', 'd':'f', 'e':'g', 'f':'h',
             'g':'i', 'h':'j', 'i':'k', 'j':'l', 'k':'m', 'l':'n',
             'm':'o', 'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t',
             's':'u', 't':'v', 'u':'w', 'v':'x', 'w':'y', 'y':'z',
             'z':'a', ' ':' '}
    
    # Initialize a variable to hold the encrypted string.
    s_encrypt = ''
    
    # Loop through each letter in the string and append the value
    # from the shift dictionary to the encrypted string.
    for letter in s:
        s_encrypt += shift[letter]
    
    # Return the encrypted string.
    return s_encrypt

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'hi'
    decrypt('lm') returns 'hi'
    decrypt('ewhjklnop') returns 'asdfghjkl'
    decrypt('kj') returns 'gf'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    # Initialize a dictionary with the letters of the alphabet as keys
    # and the letters they should be shifted to as values.
    shift = {'c':'a', 'd':'b', 'e':'c', 'f':'d', 'g':'e', 'h':'f',
             'i':'g', 'j':'h', 'k':'i', 'l