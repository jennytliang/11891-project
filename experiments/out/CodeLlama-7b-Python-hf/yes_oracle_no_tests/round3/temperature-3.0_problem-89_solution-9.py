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
    
	Do not include these tokens in the code: # my solution
	"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Create your code below:
    new_str = ""
    for ch in s:
        if ch in alphabet:
            new_str += alphabet[(alphabet.index(ch) + 2 * 2) % len(alphabet)]
        else:
            new_str += ch
    return new_str


def main():
    print(encrypt("hi"))  # > "lm"
    print(encrypt("asdfghjkl"))  # > "ewhjklnop"
    print(encrypt("gf"))  # > "kj"
    print(encrypt("et"))  # > "ix"


if __name__ == "__main__":
    main()
