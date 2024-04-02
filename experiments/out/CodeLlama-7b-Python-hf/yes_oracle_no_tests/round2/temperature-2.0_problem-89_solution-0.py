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
	Do not include these tokens in the code: shift
	"""
    result = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                result += chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
            else:
                result += chr((ord(c) - ord('A') + 2) % 26 + ord('A'))
        else:
            result += c
    return result