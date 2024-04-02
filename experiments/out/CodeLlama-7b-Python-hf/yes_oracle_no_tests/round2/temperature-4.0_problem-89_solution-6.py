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
    
	Do not include these tokens in the code: # initialize a dictionary to store
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for c in s:
        if c == ' ':
            new_s += ' '
        else:
            new_s += alphabet[alphabet.index(c) + 4]
    return new_s


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
    
	Do not include these tokens in the code: # initialize a dictionary to store
	"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for c in s:
        if c == ' ':
            new_s += ' '
        else:
            new_s += alphabet[alphabet.index(c) + 4]
    return new_s


# tests
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'


if __name__ == '__main__':
    test_encrypt()
