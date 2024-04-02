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
    e = ' zy xw vut sr qpo mn lk jih gfe dcba'
    s = s.lower()
    res = ''
    for i in s:
        if i in d:
            res += e[d.index(i)]
        else:
            res += i
    return res


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
    e = ' zy xw vut sr qpo mn lk jih gfe dcba'
    s = s.lower()
    res = ''
    for i in s:
        if i in e:
            res += d[e.index(i)]
        else:
            res += i
    return res
