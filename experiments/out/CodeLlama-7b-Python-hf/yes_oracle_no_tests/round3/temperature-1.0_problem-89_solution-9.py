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
    
	Include these tokens in the code: d = ' abc
	Do not include these tokens in the code: pass
	"""
    enc = ''
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            enc += chr(ord('a') + ((ord(i) - ord('a')) * 2) % 26)
        else:
            enc += i
    return enc
