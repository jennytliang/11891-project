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
    # s = "abcdefghijklmnopqrstuvwxyz"
    # d = "gfedcba"
    # d = "abcdefghijklmnopqrstuvwxyz"
    # return "".join([d[s.index(i)] for i in s])
    return "".join([s[(i + 2) % len(s)] for i in range(len(s))])


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'lm'
    decrypt('asdfghjkl') returns 'ewhjklnop'
    decrypt('gf') returns 'kj'
    decrypt('et') returns 'ix'
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    # s = "abcdefghijklmnopqrstuvwxyz"
    # d = "gfedcba"
    # d = "abcdefghijklmnopqrstuvwxyz"
    # return "".join([s[d.index(i)] for i in d])
    return "".join([s[(i - 2) % len(s)] for i in range(len(s))])
