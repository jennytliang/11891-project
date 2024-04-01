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
    
	Do not include these tokens in the code: ABC DEF G HI J K LM N OP Q
	"""


    
    d = 'abcdefghijklmno'
    e = 'ABCDEFGHIJKLMNO'
    d2 = d + d
    e2 = e + e
    
    result = ''
    
    for char in s:
        if char in d:
            result += d[(d.index(char) + 2) % len(d)]
        elif char in e:
            result += e[(e.index(char) + 2) % len(e)]
        else:
            result += char
    
    return result


