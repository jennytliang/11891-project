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
	Do not include these tokens in the code: encrypted
	"""
    s = s.lower()
    new = ""
    for i in s:
        if i == " ":
            new += " "
        elif i == "a":
            new += "d"
        elif i == "b":
            new += "e"
        elif i == "c":
            new += "f"
        elif i == "d":
            new += "g"
        elif i == "e":
            new += "h"
        elif i == "f":
            new += "i"
        elif i == "g":
            new += "j"
        elif i == "h":
            new += "k"
        elif i == "i":
            new += "l"
        elif i == "j":
            new += "m"
        elif i == "k":
            new += "n"
        elif i == "l":
            new += "o"
        elif i == "m":
            new += "p"
        elif i == "n":
            new += "q"
        elif i == "o":
            new += "r"
        elif i == "p":
            new += "s"
        elif i == "q":
            new += "t"
        elif i == "r":
            new += "u"
        elif i == "s":
            new += "v"
        elif i == "t":
            new += "w"
        elif i == "u":
            new += "x"
        elif i == "v":
            new += "y"
        elif i == "w":
            new += "z"
        elif i == "x":
            new += "a"
        elif i == "y":
            new += "b"
        elif i == "z":
            new += "c"
    return new


print(encrypt("hi"))
print(encrypt("asdfghjkl"))
print(encrypt("gf"))
print(encrypt("et"))
