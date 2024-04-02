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
	Do not include these tokens in the code: s
	"""
    shift = 2 * 2
    s = s.lower()
    return ''.join([chr(((ord(c) - ord('a') + shift) % 26) + ord('a')) if c.isalpha() else c for c in s])

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
    
	Include these tokens in the code: d
	Do not include these tokens in the code: s
	"""
    shift = 2 * 2
    s = s.lower()
    return ''.join([chr(((ord(c) - ord('a') - shift) % 26) + ord('a')) if c.isalpha() else c for c in s])



