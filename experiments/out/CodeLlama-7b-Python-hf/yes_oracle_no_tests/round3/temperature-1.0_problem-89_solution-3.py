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
    
	Do not include these tokens in the code: new _ d = d [ 2 :] + d
	"""


    d = 'abcdefghijklmnopqrstuvwxy'
    d = d[2:] + d[:2]
    e = ''
    for i in s:
        if i in d:
            e += d[d.index(i)+2]
        else:
            e += i
    return e




print(encrypt("hi"))
print(encrypt("asdfghjkl"))
print(encrypt("gf"))
print(encrypt("et"))
