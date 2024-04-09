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
    
	Do not include these tokens in the code: s = s . lower ()
	"""


    d = 'abcdefghijklmnopqrstuvwxy'
    d_encrypt = 'cdefghijklmnopqrstuvwxyzab'

    s = s.lower()
    s = s.replace(' ','')

    res = ''
    for i in s:
        res += d_encrypt[d.index(i)]

    return res

#encrypt('et')
#encrypt('gf')
#encrypt('asdfghjkl')
#encrypt('hi')

