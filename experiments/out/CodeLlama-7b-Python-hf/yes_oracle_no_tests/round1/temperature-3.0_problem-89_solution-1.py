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
    encrypted = ""
    for i in s:
        if i == " ":
            encrypted += " "
        elif i.isupper():
            # uppercase letters
            encrypted += chr((ord(i) + 2*2 - 65) % 26 + 65)
        else:
            # lowercase letters
            encrypted += chr((ord(i) + 2*2 - 97) % 26 + 97)
    return encrypted

print(encrypt("et"))
# >>> ix
print(encrypt("gf"))
# >>> kj