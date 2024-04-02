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
    d = ' abc def gh ij kl mn op qr st uv wx yz'
    s = s.lower()
    s2 = ''
    for c in s:
        if c in d:
            s2 += d[2*d.index(c):2*d.index(c)+2]
        else:
            s2 += c
    return s2


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
    d = ' abc def gh ij kl mn op qr st uv wx yz'
    s = s.lower()
    s2 = ''
    for c in s:
        if c in d:
            s2 += d[d.index(c)*2:d.index(c)*2+2]
        else:
            s2 += c
    return s2
