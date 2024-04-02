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
	Do not include these tokens in the code: string
	"""

def encrypt(s):
    new_str = ""
    s = s.lower()
    for i in s:
        if i == "a":
            new_str += "d"
    for i in s:
        if i == "b" or i == "c":
            new_str += "e"
        elif i == "d":
            new_str += "f"       
    for i in s:
        if i == "e":
            new_str += "g"
        elif i == "f":
            new_str += "h"
        elif i == "g" or i == "h":
            new_str += "i"
        elif i == "i":
            new_str += "j"
        elif i == "j":
            new_str += "k"
        elif i == "k":
            new_str += "l"
        elif i == "l":
            new_str += "m"
        elif i == "m":
            new_str += "n"
        elif i == "n":
            new_str += "o"
        elif i == "o":
            new_str += "p"
        elif i == "p":
            new_str += "q"
        elif i == "q":
            new_str += "r"
        elif i == "r":
            new_str += "s"
        elif i == "s":
            new_str += "t"
        elif i == "t":
            new_str += "u"
        elif i == "u":
            new_str += "v"
        elif i == "v":
            new_str += "w"
        elif i == "w":
            new_str += "x"
        elif i == "x":
            new_str += "y"
        elif i == "y":
            new_str += "z"
        elif i == "z":
            new_str += "a"
        else:
            new_str = new_str + i
    return new_str

print(encrypt("hia"))
print(encrypt("