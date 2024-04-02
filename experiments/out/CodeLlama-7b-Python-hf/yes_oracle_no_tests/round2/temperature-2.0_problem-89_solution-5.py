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
    # write your code here
    d = ' abc def gh ij kl mn op qr st uv wx yz'
    d = d.split()
    s = s.lower()
    res = ''
    for c in s:
        if c == ' ':
            res += ' '
        else:
            res += d[(d.index(c) + 2) % 26]
    return res