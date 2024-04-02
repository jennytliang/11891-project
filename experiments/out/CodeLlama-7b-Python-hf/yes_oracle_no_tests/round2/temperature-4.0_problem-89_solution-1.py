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
    
	Include these tokens in the code: abc def gh ij kl mn op q
	Do not include these tokens in the code: i j
	"""

    
    encrypted_string = ''
    alphabet = 'abcdefghijklmnopq'
    for letter in s:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + 2 * 2
            if new_index >= 20:
                new_index = new_index % 20
            encrypted_string += alphabet[new_index]
        else:
            encrypted_string += letter
    return encrypted_string
























