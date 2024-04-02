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
    return ''.join([d[(d.find(i) + 4*2) % len(d)] if i in d else i for i in s])


def decrypt(s):
    """Write a function decrypt that takes a string as an argument and
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
    d = 'abcdefghijklmnop'
    return ''.join([d[(d.find(i) - 4*2) % len(d)] if i in d else i for i in s])
