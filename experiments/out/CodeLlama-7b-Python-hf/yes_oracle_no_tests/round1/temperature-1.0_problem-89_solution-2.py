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
    
	Include these tokens in the code: d = '
	Do not include these tokens in the code: return s . translate ( str .
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    rotated = d[2:] + d[:2]
    output = ''
    for letter in s.lower():
        output_letter = rotated[rotated.index(letter) + 4]
        if letter.isupper():
            output += output_letter.upper()
        else:
            output += output_letter
    return output
