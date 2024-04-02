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
    d = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    new_s = ''
    for i in s:
        if i in d:
            new_s += d[(d.index(i) + 2 * 2) % len(d)]
        else:
            new_s += i
    return new_s


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
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    d = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    new_s = ''
    for i in s:
        if i in d:
            new_s += d[(d.index(i) - 2 * 2) % len(d)]
        else:
            new_s += i
    return new_s


print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))

print(decrypt('lm'))
print(decrypt('ewhjklnop'))
print(decrypt('kj'))
print(decrypt('ix'))