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
    
	Include these tokens in the code: return " ". join ( map ( lambda ch
	Do not include these tokens in the code: s = s . lower () new _
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    return " ".join(map(lambda ch: d[(d.find(ch) + 2*2) % len(d)], s))


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
    
	Include these tokens in the code: return " ". join ( map ( lambda ch
	Do not include these tokens in the code: s = s . lower () new _
	"""
    d = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    return " ".join(map(lambda ch: d[(d.find(ch) + 2*2) % len(d)], s))


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
    
	Include these tokens in the code: return " ". join ( map ( lambda ch
	Do not include these tokens in the code: s = s . lower () new _
	"""
    d = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    return " ".join(map(lambda ch: d[(d.find(ch) + 2*2) % len(d)], s))


def encrypt(s):
