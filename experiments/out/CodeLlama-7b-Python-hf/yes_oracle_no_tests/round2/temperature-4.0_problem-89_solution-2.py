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
    
	Include these tokens in the code: abc
	"""

    
    # Write your code here. 
    a = 'abc'
    s = list(s)
    for i in range(len(s)):
        if s[i] in a:
            s[i] = a[(a.index(s[i]) + 4) % 26]
    return ''.join(s)
