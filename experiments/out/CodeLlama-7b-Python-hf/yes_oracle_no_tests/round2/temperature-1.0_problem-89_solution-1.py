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
    
	Include these tokens in the code: return " ". join ( map ( lambda ch :
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    n = 'abcdefghijklmnopqrstuvwxyz'
    p = ''
    for ch in s:
        if ch in d:
            p += n[d.index(ch)]
        else:
            p += ch
    return p


print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))
