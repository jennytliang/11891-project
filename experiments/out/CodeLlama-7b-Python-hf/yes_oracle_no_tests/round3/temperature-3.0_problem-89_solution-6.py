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
	Do not include these tokens in the code: # create a list of
	"""
    # create a list of letters in the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # create a list of encrypted letters
    encrypted_letters = 'cdefghijklmnopqrstuvwxyzab'
    # create a dictionary that maps the letters to encrypted letters
    d = dict(zip(letters, encrypted_letters))
    # create a string that is the encrypted string
    encrypted_string = ''
    for letter in s:
        if letter in letters:
            # add the encrypted letter to the string
            encrypted_string += d[letter]
        else:
            # add the letter to the string
            encrypted_string += letter
    # return the encrypted string
    return encrypted_string

def encrypt2(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_letters = 'cdefghijklmnopqrstuvwxyzab'
    d = dict(zip(letters, encrypted_letters))
    # create a string that is the encrypted string
    encrypted_string = ''
    for letter in s:
        if letter in letters:
            # add the encrypted letter to the string
            encrypted_string += d[letter]
        else:
            # add the letter to the string
            encrypted_string += letter
    # return the encrypted string
    return encrypted_string

def main():
    #base = input('Enter a string: ')
    #print(encrypt(base))
    print(encrypt('hi'))
    print(encrypt('asdfghjkl'))
    print(encrypt('gf'))
    print(encrypt('et'))
main()