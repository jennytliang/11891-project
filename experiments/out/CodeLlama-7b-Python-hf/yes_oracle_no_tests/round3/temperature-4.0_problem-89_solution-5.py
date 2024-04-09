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
    
	Include these tokens in the code: d = ' abc
	Do not include these tokens in the code: pass
	"""
    d = ' abcdefghijklmnopqrstuvwxyz'
    r = ''
    for c in s:
        r += d[(d.find(c)+2)%len(d)]
    return r


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'mn'
    decrypt('asdfghjkl') returns 'qwertyuiop'
    decrypt('gf') returns 'bc'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d = ' abc
	Do not include these tokens in the code: pass
	"""
    d = ' abcdefghijklmnopqrstuvwxyz'
    r = ''
    for c in s:
        r += d[(d.find(c)-2)%len(d)]
    return r


def main():
    """Print the results of the encryption and decryption functions."""
    print(encrypt('hi'))
    print(encrypt('asdfghjkl'))
    print(encrypt('gf'))
    print(encrypt('et'))
    print(decrypt('hi'))
    print(decrypt('asdfghjkl'))
    print(decrypt('gf'))
    print(decrypt('ix'))


if __name__ == '__main__':
    main()
