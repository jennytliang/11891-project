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
	Do not include these tokens in the code: # Your code here pass
	"""
    s = s.lower()
    result = ""
    for i in s:
        if i in 'abc':
            result += 'd'
        elif i in 'def':
            result += 'e'
        elif i in 'ghi':
            result += 'f'
        elif i in 'jkl':
            result += 'g'
        elif i in 'mno':
            result += 'h'
        elif i in 'pqrs':
            result += 'i'
        elif i in 'tuv':
            result += 'j'
        elif i in 'wxyz':
            result += 'k'
        elif i in ' ':
            result += ' '
    return result

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d = ' abc
	Do not include these tokens in the code: # Your code here pass
	"""
    s = s.lower()
    result = ""
    for i in s:
        if i in 'd':
            result += 'abc'
        elif i in 'e':
            result += 'def'
        elif i in 'f':
            result += 'ghi'
        elif i in 'g':
            result += 'jkl'
        elif i in 'h':
            result += 'mno'
        elif i in 'i':
            result += 'pqrs'
        elif i in 'j':
            result += 'tuv'
        elif i in 'k':
            result += 'wxyz'
        elif i in ' ':
            result += ' '
    return result