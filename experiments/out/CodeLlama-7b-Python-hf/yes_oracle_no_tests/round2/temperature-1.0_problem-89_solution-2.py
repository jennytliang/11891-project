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
    
	Include these tokens in the code: " ". join ( map ( lambda ch : chr
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    r = ''.join(map(lambda ch: chr((((ord(ch) - ord('a') + 2) % 26) + ord('a'))), s))
    return r


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'qx'
    decrypt('asdfghjkl') returns 'vwzyx'
    decrypt('gf') returns 'mn'
    decrypt('et') returns 'qv'
    
	Include these tokens in the code: " ". join ( map ( lambda ch : chr
	"""

    d = 'abcdefghijklmnopqrstuvwxyz'
    r = ''.join(map(lambda ch: chr((((ord(ch) - ord('a') - 2) % 26) + ord('a'))), s))
    return r


def main():
    """Print out the results of encrypting the input string.
    If the input string is not a string, print out an error.
    """

    s = input('Please enter a string: ')
    if type(s) == str:
        print(encrypt(s))
    else:
        print('Error: input is not a string!')


if __name__ == '__main__':
    main()
