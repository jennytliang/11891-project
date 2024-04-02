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
    
	Include these tokens in the code: d = '
	Do not include these tokens in the code: return s . translate ( str .
	"""
    s = str(s)


    d = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    result = ""
    for i in s:
        if i in d:
            result += d[(d.index(i) + 40) % len(d)]
        else:
            result += i
    return result

print(encrypt("hi"))
print(encrypt("asdfghjkl"))
print(encrypt("gf"))
print(encrypt("et"))

#test.assert_equals(encrypt('thequickbrownfoxjumped'), 'sxwzrvjklmyzea')
#test.assert_equals(encrypt('TheQuickBrownFoxJumped'), 'SoWoVnNnVilYhA')
#test.assert_equals(encrypt('e'), 'i')


# Create a function decrypt that takes a string as an argument
# and returns a string that is the decrypted message.
# The alphabet should be rotated back by two places.
# The decrytion method should only be used when the string is encrypted with
# the encrypt function. For example:
# decrypt('lm')  returns 'hi'
# decrypt('ewhjklnop') returns 'asdfghjkl' 
# decrypt('kj') returns 'gf'
# decrypt('ix') returns 'et'
# Create a function generate_key(strlen, keylen) that takes the length of
# the string to be encrypted in characters,
# and the length of the alphabet to be rotated,
# as parameters. 
# It should generate a key string using integers as characters. 
# For example, generate_key(11, 18) returns '225311321214931832618',
# and generate_key(11, 2) returns: '43531132121493183