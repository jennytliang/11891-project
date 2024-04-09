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
    
	Do not include these tokens in the code: s = s . lower ()
	"""
    new_str = ""
    for i in s:
        new_str += chr(((ord(i) - ord('a') + 2) * 2) % 26 + ord('a'))
    return new_str


def main():
    print(encrypt("hi"))
    print(encrypt("asdfghjkl"))
    print(encrypt("gf"))
    print(encrypt("et"))


if __name__ == "__main__":
    main()
