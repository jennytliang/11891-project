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
	Do not include these tokens in the code: # Set the alphabet
	"""
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'cdefghijklmnopqrstuvwxyzab'
    c = ''
    for i in s:
        if i in a:
            c += b[a.index(i)]
        else:
            c += i
    return c


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
	Do not include these tokens in the code: # Set the alphabet
	"""
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'cdefghijklmnopqrstuvwxyzab'
    c = ''
    for i in s:
        if i in a:
            c += b[a.index(i)]
        else:
            c += i
    return c


# tests
print('-- Encrypt Tests --')
assert encrypt('hi') == 'lm'
assert encrypt('asdfghjkl') == 'ewhjklnop'
assert encrypt('gf') == 'kj'
assert encrypt('et') == 'ix'
print('All tests passed!')

# tests
print('-- Decrypt Tests --')
assert decrypt('lm') == 'hi'
assert decrypt('ewhjklnop') == 'asdfghjkl'
assert decrypt('kj') == 'gf'
assert decrypt('ix') == 'et'
print('All tests passed!')

# test 2
print('-- Test 2 --')
assert encrypt(decrypt('lm')) == 'hi'