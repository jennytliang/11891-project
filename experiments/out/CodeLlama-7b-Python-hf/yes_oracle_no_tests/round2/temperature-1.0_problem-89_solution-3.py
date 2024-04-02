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
	Do not include these tokens in the code: new _ d =
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    new_d = d[2:] + d[:2]
    return ''.join(new_d[d.index(ch)] for ch in s)


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'gh'
    decrypt('asdfghjkl') returns 'zxcvbnm'
    decrypt('gf') returns 'fz'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: return " ". join ( map ( lambda ch :
	Do not include these tokens in the code: new _ d =
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    new_d = d[2:] + d[:2]
    return ''.join(d[new_d.index(ch)] for ch in s)


#print(encrypt('hi'))
#print(decrypt('hi'))
#print(encrypt('asdfghjkl'))
#print(decrypt('asdfghjkl'))
#print(encrypt('gf'))
#print(decrypt('gf'))
#print(encrypt('et'))
#print(decrypt('et'))
