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
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: rot ated = d [ 2 :] + d [:
	"""


    d = 'abcdefghijklmnopqrstuvwxy'
    
    return " ".join([(d[d.index(char) % len(d)] if d.index(char) % len(d)>=2
                     else d[d.index(char) % len(d)]) 
                   for char in s.lower()]).lower()
