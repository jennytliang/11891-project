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
    """
    alphas = list('abcdefghijklmnopqrstuvwxyz')
    alphas_copy = alphas.copy()
    result = ''
    for i, letter in enumerate(s):
        # print(alphas)
        if letter.islower():
            # print(alphas)
            shift_index = alphas_copy.index(letter)
            # print(shift_index)
            result += alphas[shift_index + 2]
            # alphas.pop(shift_index)
            alphas_copy.pop(shift_index)
        else:
            shift_index = alphas_copy.index(letter.lower())
            result += alphas[shift_index + 2].upper()
    return result