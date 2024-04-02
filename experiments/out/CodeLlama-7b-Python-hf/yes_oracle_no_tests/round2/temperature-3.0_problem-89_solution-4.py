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
	Do not include these tokens in the code: s
	"""
    # TODO: Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_s = ""
    for i in s:
        if i in alphabet:
            new_s += alphabet[(alphabet.index(i) + 4) % len(alphabet)]
        else:
            new_s += i
    return new_s


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: s
	"""
    # TODO: Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_s = ""
    for i in s:
        if i in alphabet:
            new_s += alphabet[(alphabet.index(i) - 4) % len(alphabet)]
        else:
            new_s += i
    return new_s


print(encrypt("hi"))
print(encrypt("asdfghjkl"))
print(encrypt("gf"))
print(encrypt("et"))
print(decrypt("lm"))
print(decrypt("ewhjklnop"))
print(decrypt("kj"))
print(decrypt("ix"))
