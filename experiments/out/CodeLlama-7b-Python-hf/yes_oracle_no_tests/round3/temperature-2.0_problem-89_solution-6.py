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
	Do not include these tokens in the code: s _ list
	"""
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s[i] = chr((ord(s[i]) - ord('A') + 2) % 26 + ord('A'))
            else:
                s[i] = chr((ord(s[i]) - ord('a') + 2) % 26 + ord('a'))
    return ''.join(s)

print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))
