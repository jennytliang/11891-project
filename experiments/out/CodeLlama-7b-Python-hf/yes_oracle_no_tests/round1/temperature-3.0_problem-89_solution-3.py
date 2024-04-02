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
	Do not include these tokens in the code: encrypted
	"""
    # create a dictionary of characters and their new values
    new_vals = {}
    for char in s:
        if char.isalpha():
            if char.isupper():
                new_vals[char] = chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                new_vals[char] = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            new_vals[char] = char
    # return the new string
    return ''.join(new_vals[char] for char in s)
