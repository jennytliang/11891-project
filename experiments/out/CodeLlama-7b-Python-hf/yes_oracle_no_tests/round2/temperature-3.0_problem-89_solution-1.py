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
    d = ' abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    new_s = ''
    for i in s:
        new_s += d[d.find(i) + 2]
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
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    d = ' abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    new_s = ''
    for i in s:
        new_s += d[d.find(i) + 2]
    return new_s


# tests
def test_encrypt():
    string1 = "hi"
    string2 = "asdfghjkl"
    string3 = "gf"
    string4 = "et"
    assert encrypt(string1) == "lm"
    assert encrypt(string2) == "ewhjklnop"
    assert encrypt(string3) == "kj"
    assert encrypt(string4) == "ix"

