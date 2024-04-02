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

    # initialize a dictionary to store the letters and their rotated values
    d = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
         'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
         'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
         'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
         'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a',
         'z': 'b'}
    
    # initialize a list to store the rotated letters
    l = []
    
    # loop through the string and replace each letter with its rotated value
    for i in s:
        l.append(d[i])
        
    # return the string with the rotated letters
    return ''.join(l)
    
def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('lm') returns 'hi'
    decrypt('ewhjklnop') returns 'asdfghjkl'
    decrypt('kj') returns 'gf'
    decrypt('ix') returns 'et'
    
    Include these tokens in the code: d = ' abc def gh ij kl mn op
    """
    
    # initialize a dictionary to store the letters and their rotated values
    d = {'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
         'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
         '