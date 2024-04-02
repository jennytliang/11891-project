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
    d = 'abcdefghijklmnop'
    e = 'cdefghijklmnopab'
    out = ''

    for char in list(s):
        if char.isalpha():
            if char.lower() in d:
                out += e[d.index(char.lower())]
            elif char.lower() in e:
                out += d[e.index(char.lower())]
        else:
            out += char
    return out
    
