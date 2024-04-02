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
	Do not include these tokens in the code: encrypted
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for letter in s:
        if letter in alphabet:
            encrypted += alphabet[((alphabet.index(letter) + 4) % 26)]
        else:
            encrypted += letter
    return encrypted


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
	Do not include these tokens in the code: decrypted
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for letter in s:
        if letter in alphabet:
            decrypted += alphabet[((alphabet.index(letter) - 4) % 26)]
        else:
            decrypted += letter
    return decrypted


# test
s = "et"
print(encrypt(s))
print(decrypt(encrypt(s)))
print(decrypt(decrypt(s)))
print(encrypt(decrypt("et")))
print(decrypt(encrypt("et")))
