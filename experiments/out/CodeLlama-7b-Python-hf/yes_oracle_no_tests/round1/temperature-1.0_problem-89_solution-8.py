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
    d = ' abcdefghijklmnop'
    s = s.lower()
    new_string = ''
    for letter in s:
        if letter in d:
            new_string += d[(d.index(letter) + 2) % len(d)]
        else:
            new_string += letter
    return new_string


def encrypt_2(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d = ' abcdefghijklmnop
	"""
    d = ' abcdefghijklmnop'
    s = s.lower()
    new_string = ''
    for letter in s:
        if letter in d:
            new_string += d[(d.index(letter) + 4) % len(d)]
        else:
            new_string += letter
    return new_string
