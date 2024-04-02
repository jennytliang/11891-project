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
    
	Do not include these tokens in the code: # create a dictionary that maps
	"""
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = chr(ord(s[i]) + 2*26)
    return "".join(s)


def main():
    print(encrypt("hi"))
    print(encrypt("asdfghjkl"))
    print(encrypt("gf"))
    print(encrypt("et"))


if __name__ == "__main__":
    main()
