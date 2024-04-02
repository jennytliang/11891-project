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
	Do not include these tokens in the code: print ( s ) c
	"""
# This section is used to display error message if user did not enter any string
    if not s:
        print("There is no text entered.")
    else:
        encrypted = ""
        for char in s:
            if char != " ":
                if char.isupper():
                    encrypted += chr((ord(char) + (ord('D') * 2)) % 26 + ord('A'))
                else:
                    encrypted += chr((ord(char) + (ord('d') * 2)) % 26 + ord('a'))
        return encrypted
