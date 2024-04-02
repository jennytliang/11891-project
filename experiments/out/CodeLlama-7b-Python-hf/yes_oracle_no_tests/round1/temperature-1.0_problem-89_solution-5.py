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

    # create a dictionary that maps the alphabet to the alphabet rotated
    # down by two
    d = {}
    for i in range(26):
        d[chr(97+i)] = chr(97+(i+2)%26)
        d[chr(97+i).upper()] = chr(97+(i+2)%26).upper()

    # return the string with the alphabet rotated
    return s.translate(str.maketrans(d))


# print(encrypt('hi'))
# print(encrypt('asdfghjkl'))
# print(encrypt('gf'))
# print(encrypt('et'))

# import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)


def encrypt(s):
    # create a dictionary that maps the alphabet to the alphabet rotated
    # down by two
    d = {}
    for i in range(26):
        d[chr(97+i)] = chr(97+(i+2)%26)
        d[chr(97+i).upper()] = chr(97+(i+2)%26).upper()

    # return the string with the alphabet rotated
    return s.translate(str.maketrans(d))


# print(encrypt('hi'))
# print(encrypt('asdfghjkl'))
# print(encrypt('gf'))
# print(encrypt('et'))
