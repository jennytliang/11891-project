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
    
	Include these tokens in the code: d = ' abc def gh ij kl mn op
	"""
    
    # my solution
    # d = ' abcdefghijklmnopqrstuvwxyz'
    # d_rev = d[::-1]
    # new_s = ''
    # for i in s:
    #     if i in d:
    #         new_s += d_rev[d.index(i) * 2 * 2]
    #     else:
    #         new_s += i
    # return new_s
    
    # solution 1
    # return s.translate(str.maketrans(d, d[2:] + d[:2]))
    
    # solution 2
    # return s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'))
    
    # solution 3
    d = ' abcdefghijklmnopqrstuvwxyz'
    d_rev = d[::-1]
    new_s = ''
    for i in s:
        if i in d:
            new_s += d_rev[d.index(i) * 2 * 2]
        else:
            new_s += i
    return new_s


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'lm'
    decrypt('asdfghjkl') returns 'ewhjklnop'
    decrypt('gf') returns 'kj'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d = ' abcdefghijklmnopqrstuvwxyz'
	"""
    
    # my solution
    # d = ' abcdefghijklmnopqrstuvwxyz'
    # d_rev = d[::-1]
    #