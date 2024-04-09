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
    
	Do not include these tokens in the code: s = s . lower ()
	"""
    return s.lower().translate(str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "cdefghijklmnopqrstuvwxyzab"
    ))


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'lm'
    decrypt('asdfghjkl') returns 'ewhjklnop'
    decrypt('gf') returns 'kj'
    decrypt('ix') returns 'et'
    
	Do not include these tokens in the code: s = s . lower ()
	"""
    return s.lower().translate(str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "cdefghijklmnopqrstuvwxyzab"
    ))[::-1]
