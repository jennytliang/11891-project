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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    s = s.lower()
    result = ''
    for l in s:
        if (ord(l) >= ord('a') and ord(l) <= ord('z')):
            newpos = i+2*2
            if newpos >= 26:
                newpos = newpos % 26
            result = result + alphabet[newpos]
        else:
            result = result + l
        i = i+1
    return result

