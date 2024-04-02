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
    
	Include these tokens in the code: q r st uv w xyz
	"""

    d = 'abcdefghijklnmopqrstuvwxyz'
    e = 'qrstuvwxyzabcdefghijklmnop'
    s = s.lower()
    r = ''
    for i in s:
        if i in d:
            r += e[d.index(i)]
        else:
            r += i
    return r


print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))
