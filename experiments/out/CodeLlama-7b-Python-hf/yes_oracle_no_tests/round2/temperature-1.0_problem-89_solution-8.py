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
    
	Include these tokens in the code: abc
	"""

    
    alphabet = 'abc'
    s_encrypted = ''
    for letter in s:
        if letter in alphabet:
            s_encrypted += alphabet[(alphabet.index(letter) + 2) % len(alphabet)]
        else:
            s_encrypted += letter
    return s_encrypted


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
    
	Include these tokens in the code: abc
	"""

    
    alphabet = 'abc'
    s_decrypted = ''
    for letter in s:
        if letter in alphabet:
            s_decrypted += alphabet[(alphabet.index(letter) - 2) % len(alphabet)]
        else:
            s_decrypted += letter
    return s_decrypted
