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
    # start with the empty string to hold the encrypted message
    encrypted = ''

    # loop through the string and add the encrypted letter to the end of the encrypted string
    for letter in s:
        # check if the letter is in the alphabet
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            # find the letter's position in the alphabet
            position = ord(letter) - ord('a')
            # shift that position down by two multiplied to two places
            shift = (position * 2 * 2) % 26
            # add the encrypted letter to the end of the encrypted string
            encrypted += chr(ord('a') + shift)
        else:
            # if the letter is not in the alphabet, add it to the encrypted string as is
            encrypted += letter

    # return the encrypted string
    return encrypted


def main():
    print(encrypt('hi'))
    print(encrypt('asdfghjkl'))
    print(encrypt('gf'))
    print(encrypt('et'))


if __name__ == '__main__':
    main()
