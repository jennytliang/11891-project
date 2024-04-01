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

    encrypted = []

    alphabet_set = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(s)):

        alphabet = s[i]
        alphabet_index = alphabet_set.index(alphabet)

        if i % 2 == 0:
            new_alphabet_index = alphabet_index + 2
        else:
            new_alphabet_index = alphabet_index - 2

        if alphabet_index < 0:
            new_alphabet_index = len(alphabet_set) + alphabet_index

        new_alphabet = alphabet_set[new_alphabet_index]

        encrypted.append(new_alphabet)

    return "".join(encrypted)


