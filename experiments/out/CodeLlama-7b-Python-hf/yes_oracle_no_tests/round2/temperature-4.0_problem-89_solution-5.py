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
    
	Include these tokens in the code: abc def gh ij kl mn op q
	Do not include these tokens in the code: i j
	"""

    
    pass


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
    
	Include these tokens in the code: abc def gh ij kl mn op q
	Do not include these tokens in the code: i j
	"""

    
    pass


if __name__ == '__main__':
    print(encrypt('hi'))
    print(encrypt('asdfghjkl'))
    print(encrypt('gf'))
    print(encrypt('et'))

    print(decrypt('lm'))
    print(decrypt('ewhjklnop'))
    print(decrypt('kj'))
    print(decrypt('ix'))
