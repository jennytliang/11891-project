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
	Do not include these tokens in the code: # Create a dictionary
	"""
    new_dict = {}
    for i in range(26):
        new_dict[chr(ord('a') + i)] = chr(ord('d') + i*2)
    new_dict[' '] = ' '
    new_dict['\n'] = '\n'
    encrypted_string = ''
    for char in s:
        if char in new_dict:
            encrypted_string += new_dict[char]
        else:
            encrypted_string += char
    return encrypted_string


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'lm'
    decrypt('asdfghjkl') returns 'ewhjklnop'
    decrypt('gf') returns 'kj'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: # Create a dictionary
	"""
    new_dict = {}
    for i in range(26):
        new_dict[chr(ord('d') + i*2)] = chr(ord('a') + i)
    new_dict[' '] = ' '
    new_dict['\n'] = '\n'
    encrypted_string = ''
    for char in s:
        if char in new_dict:
            encrypted_string += new_dict[char]
        else:
            encrypted_string += char
    return encrypted_string


def main():
    """
    Use the functions to encrypt and decrypt the following messages.
    """
    print(encrypt('hi'))
    print(decrypt('lm'))
    print(encrypt('asdfghjkl'))
    print(decrypt('ewhjklnop'))
    print(encrypt('gf'))
    print(decrypt('kj'))
    print(encrypt('et'))
    print(