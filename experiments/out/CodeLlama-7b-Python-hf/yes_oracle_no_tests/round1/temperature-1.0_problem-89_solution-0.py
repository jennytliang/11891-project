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

    string = 'abcdefghijklmnopqrstuvwxyz'
    string += string.upper()
    shifted_string = s[0:][::-1] + s[1:]
    replace_string = string
    replaced_string = shifted_string.translate(str.maketrans(string, replace_string))
    encrypted = replaced_string[::-1]
    return encrypted

    """Write your code below this row  #######################################"""


s = input('Enter a string: ')
print(encrypt(s))





