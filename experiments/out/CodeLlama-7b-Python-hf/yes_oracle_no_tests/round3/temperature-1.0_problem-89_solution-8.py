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
    
	Include these tokens in the code: d
	Do not include these tokens in the code: alphabet
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    out = []
    for c in s:
        if c in alphabet:
            out.append(alphabet[(alphabet.index(c)+2*2)%len(alphabet)])
        else:
            out.append(c)
    return ''.join(out)

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'gh'
    decrypt('asdfghjkl') returns 'zxcvbnm'
    decrypt('gf') returns 'bc'
    decrypt('et') returns 'dx'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: alphabet
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    out = []
    for c in s:
        if c in alphabet:
            out.append(alphabet[(alphabet.index(c)-2*2)%len(alphabet)])
        else:
            out.append(c)
    return ''.join(out)
