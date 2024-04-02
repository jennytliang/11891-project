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
    l = list(s)
    for i in range(len(l)):
        if l[i] in 'abcdefghijklmnopqrstuvwxyz':
            l[i] = 'abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'
                    .find(l[i]) + 2 * 2) % 26]
    return ''.join(l)


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    l = list(s)
    for i in range(len(l)):
        if l[i] in 'abcdefghijklmnopqrstuvwxyz':
            l[i] = 'abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'
                    .find(l[i]) + 2 * -2) % 26]
    return ''.join(l)
