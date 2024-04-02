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
	Do not include these tokens in the code: # s
	"""
    s_list = list(s)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(s_list)):
        if s_list[i].lower() in alphabet:
            s_list[i] = alphabet[(alphabet.index(s_list[i].lower()) + 2*2) % len(alphabet)]
    return "".join(s_list)



    


    








