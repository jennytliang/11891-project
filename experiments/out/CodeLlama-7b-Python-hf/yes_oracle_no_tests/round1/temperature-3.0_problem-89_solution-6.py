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
    s = s.lower()
    return ''.join([chr((ord(i) - 97 + 2 * 2) % 26 + 97) if i.isalpha() else i for i in s])


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
    
	Include these tokens in the code: d
	Do not include these tokens in the code: encrypted
	"""
    s = s.lower()
    return ''.join([chr((ord(i) - 97 - 2 * 2) % 26 + 97) if i.isalpha() else i for i in s])


def main():
    # encrypt("hi") # returns "lm"
    # decrypt("hi") # returns "lm"
    print(encrypt('hi'))
    print(decrypt('lm'))
    print(encrypt('asdfghjkl'))
    print(decrypt('ewhjklnop'))
    print(encrypt('gf'))
    print(decrypt('kj'))
    print(encrypt('et'))
    print(decrypt('ix'))


if __name__ == '__main__':
    main()
