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
    
	Do not include these tokens in the code: # TODO : write your answer between
	"""
    # TODO : write your answer between
    return ''.join([chr((ord(c) + 4*2 - 97) % 26 + 97) for c in s])


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
    
	Do not include these tokens in the code: # TODO : write your answer between
	"""
    # TODO : write your answer between
    return encrypt(s)


# encrypt('hi')
# encrypt('asdfghjkl')
# encrypt('gf')
# encrypt('et')
