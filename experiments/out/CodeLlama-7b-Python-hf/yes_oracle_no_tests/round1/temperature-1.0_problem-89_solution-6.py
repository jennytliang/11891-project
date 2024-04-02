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
    
	Include these tokens in the code: d = '
	Do not include these tokens in the code: return s . translate ( str .
	"""
    return ''.join([chr(ord('a')+(ord(c)-ord('a')+2)%26) if (c.islower() or c.isalpha()== False)  else chr(ord('A')+(ord(c)-ord('A')+2)%26) for c in s ])    

if __name__ == '__ main ':
    strings = ["hi", "asdfghjkl", "gf", "et"]

    for s in strings:
        print(encrypt(s))


    #    Expected Results 
    #    
    #    encrypt('hi') returns 'lm'
    #    encrypt('asdfghjkl') returns 'ewhjklnop'
    #    encrypt('gf') returns 'kj'
    #    encrypt('et') returns 'ix'
    #    encrypt('wc') = 'zb'
    #    encrypt('316th') = '909th'
