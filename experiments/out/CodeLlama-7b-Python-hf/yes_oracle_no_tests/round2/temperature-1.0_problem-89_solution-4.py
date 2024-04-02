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
	Do not include these tokens in the code: new _ s = s . encode
	"""
    new_s = ''
    alphabet_original = "abcdefghijklmnopqrstuvwxyz"
    alphabet = "cdefghijklmnopqrstuvwxyz" + alphabet_original
    for char in s:
        new_s += alphabet[alphabet.find(char)+2]
    return new_s
    
