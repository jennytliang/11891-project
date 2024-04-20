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
	Do not include these tokens in the code: l = list ( s )
	"""
    # Your code here
    d = dict(zip("abcdefghijklmnopqrstuvwxyz",
                 "cdefghijklmnopqrstuvwxyzab"))
    return "".join(d[c] if c in d else c for c in s.lower())


def main():
    print(encrypt("hi"))
    print(encrypt("asdfghjkl"))
    print(encrypt("gf"))
    print(encrypt("et"))


if __name__ == "__main__":
    main()