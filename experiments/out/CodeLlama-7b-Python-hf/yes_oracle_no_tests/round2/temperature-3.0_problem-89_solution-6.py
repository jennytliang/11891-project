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
    
    # create a list of the alphabet
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # create a list of the alphabet shifted by two (multiplied by 2)
    alphabet_shifted = list("cdefghijklmnopqrstuvwxyzab")
    
    # create an empty string
    result = ""
    
    # for each letter in the string
    for letter in s:
        # if the letter is in the alphabet
        if letter in alphabet:
            # add the letter from the shifted alphabet
            result += alphabet_shifted[alphabet.index(letter)]
        # if the letter is not in the alphabet
        else:
            # add the letter to the result
            result += letter
            
    return result


def main():
    print(encrypt("hi"))
    print(encrypt("asdfghjkl"))
    print(encrypt("gf"))
    print(encrypt("et"))


if __name__ == "__main__":
    main()
