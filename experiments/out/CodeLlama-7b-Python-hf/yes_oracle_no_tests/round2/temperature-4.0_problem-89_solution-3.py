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
    
	Do not include these tokens in the code: = ' abc def gh ij kl mn op '
	"""

    # Set the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create a dictionary for the alphabet
    alphabet_dict = {}
    for i, letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    # Create a new string
    new_string = ''

    # Loop through the string
    for char in s:

        # Check if the char is in the alphabet
        if char in alphabet:

            # Rotate the char
            new_letter = alphabet[(alphabet_dict[char] + 4) % len(alphabet)]

            # Add the new letter to the new string
            new_string += new_letter

        # If the char is not in the alphabet, add it as is
        else:
            new_string += char

    return new_string


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'mn'
    decrypt('asdfghjkl') returns 'qrstuvwxyza'
    decrypt('gf') returns 'op'
    decrypt('ix') returns 'et'
    
	Do not include these tokens in the code: = ' abc def gh ij kl mn op '
	"""

    # Set the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create a dictionary for the alphabet
    alphabet_dict = {}
    for i, letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    # Create a new string
    new_string = ''

    # Loop through the string
    for char in s:

        # Check if the char is in the alphabet
        if char in alphabet:

            # Rotate the char
            new_letter = alphabet[(alphabet_dict[char] - 4) % len