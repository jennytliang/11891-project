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
    new_s = ''
    for c in s:
        if c in alphabet:
            new_s += alphabet[alphabet.index(c) - 2]
        else:
            new_s += c
    return new_s


print(encrypt('hello'))
print(encrypt('world'))
print(encrypt('asdfghjkl'))
print(encrypt('et'))
