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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for char in s:
        if char in alphabet:
            new_string += alphabet[(alphabet.find(char) + 4) % len(alphabet)]
        else:
            new_string += char
    return new_string


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'mn'
    decrypt('asdfghjkl') returns 'zxcvbnmqr'
    decrypt('gf') returns 'op'
    decrypt('et') returns 'uy'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: s
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for char in s:
        if char in alphabet:
            new_string += alphabet[(alphabet.find(char) - 4) % len(alphabet)]
        else:
            new_string += char
    return new_string


def encrypt_decrypt(s):
    """Create a function encrypt_decrypt that takes a string as an 
    argument and returns a string encrypted and decrypted with the 
    alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt_decrypt('hi') returns 'mn'
    encrypt_decrypt('asdfghjkl') returns 'zxcvbnmqr'
    encrypt_decrypt('gf') returns 'op'
    encrypt_decrypt('et') returns 'uy'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: s
	"""
    alphabet = 'abcdefghij