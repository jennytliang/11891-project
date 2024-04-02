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
    s = s.lower()
    d = 'abcdefghijklmnopqrstuvwxyz'
    e = 'cdefghijklmnopqrstuvwxyzab'
    return s.translate(str.maketrans(d, e))


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. The alphabet 
    should be rotated in a manner such that the letters shift down by two 
    multiplied to two places.
    For example:
    decrypt('hi') returns 'hm'
    decrypt('asdfghjkl') returns 'fedbacdefg'
    decrypt('gf') returns 'bj'
    decrypt('et') returns 'hx'
    
	Include these tokens in the code: d = '
	Do not include these tokens in the code: return s . translate ( str .
	"""
    s = s.lower()
    d = 'abcdefghijklmnopqrstuvwxyz'
    e = 'cdefghijklmnopqrstuvwxyzab'
    return s.translate(str.maketrans(e, d))


# 🚨 Don't change the code below 👇
test_text = "Hello World!"
print("Original Text: " + test_text)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

encrypted_text = encrypt(test_text)
print("Encrypted Text: " + encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Decrypted Text: " + decrypted_text)
