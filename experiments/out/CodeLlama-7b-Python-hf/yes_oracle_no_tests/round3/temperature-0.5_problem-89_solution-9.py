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
    
	Include these tokens in the code: mn op q r st uv w xyz
	Do not include these tokens in the code: m no
	"""



    
    d = 'mnopqrstuvwxyz'
    e = 'mnoqrstuvwxyz'
    d = d.replace('m', '')
    e = e.replace('m', '')
    
    return s.translate(str.maketrans(d, e))










































