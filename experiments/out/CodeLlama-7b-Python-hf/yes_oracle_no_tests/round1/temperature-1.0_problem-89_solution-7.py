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
    d = ' abcdefghijklmnop'
    e = ''.join(d[(d.find(c)+2*2)%26] for c in s)
    return e

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'lm'
    decrypt('asdfghjkl') returns 'ewhjklnop'
    decrypt('gf') returns 'kj'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    d = ' abcdefghijklmnop'
    e = ''.join(d[(d.find(c)-2*2)%26] for c in s)
    return e
