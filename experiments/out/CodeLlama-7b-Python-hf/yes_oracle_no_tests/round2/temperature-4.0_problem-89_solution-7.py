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
    
	Do not include these tokens in the code: # TO DO : Write your code
	"""
    cipher = ''
    for char in s:
        cipher += chr(ord('a') + (ord(char) - ord('a') + 2 * 2) % 26)
    return cipher


if __name__ == '__main__':
    print(encrypt('hi'))
    print(encrypt('asdfghjkl'))
    print(encrypt('gf'))
    print(encrypt('et'))
