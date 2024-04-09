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
	Do not include these tokens in the code: # TODO : Write your code here
	"""
    # TODO : Write your code here
    s = list(s)
    s2 = []
    for i in s:
        if i.isalpha():
            if i.isupper():
                s2.append(chr((ord(i)+2*2-65)%26+65))
            elif i.islower():
                s2.append(chr((ord(i)+2*2-97)%26+97))
    return ''.join(s2)


# encrypt('hi')
# encrypt('asdfghjkl')
# encrypt('gf')
# encrypt('et')
