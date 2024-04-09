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
	Do not include these tokens in the code: s
	"""
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "cdefghijklmnopqrstuvwxyzab"
    c = ""
    for i in s:
        if i in a:
            c += b[a.index(i)]
        else:
            c += i
    return c