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

    s = s.lower()
    d = 'abcdefghijklmnop'
    r = ''

    for c in s:
        if c in d:
            i = d.find(c)-3
            while i >= 0:
                i = i+26
            r += i
        else:
            r += c
    return r
