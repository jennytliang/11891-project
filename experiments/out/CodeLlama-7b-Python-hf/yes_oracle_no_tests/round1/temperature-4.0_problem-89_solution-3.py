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
    d = ' abcdefghijklmnop'
    e = 'abcdefghijklmnop '
    assert type(s) == str, "Input must be a string"
    assert len(s) > 0, "Input string must be longer than 0 characters"
    assert s.isalpha(), "Input must be alphabetical"
    s = s.lower()
    new_s = ''
    for i in s:
        if i in d:
            new_s += e[d.find(i)]
        else:
            new_s += i
    return new_s
