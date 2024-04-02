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
	Do not include these tokens in the code: new _ str = '' for char in
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    d_new = d[2:] + d[:2]
    return ''.join([d_new[d.index(char)] for char in s])


print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))
