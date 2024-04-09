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
	Do not include these tokens in the code: encrypt
	"""
    
    s = s.lower()
    s = s.replace("a", "d")
    s = s.replace("b", "e")
    s = s.replace("c", "f")
    s = s.replace("d", "g")
    s = s.replace("e", "h")
    s = s.replace("f", "i")
    s = s.replace("g", "j")
    s = s.replace("h", "k")
    s = s.replace("i", "l")
    s = s.replace("j", "m")
    s = s.replace("k", "n")
    s = s.replace("l", "o")
    s = s.replace("m", "p")
    s = s.replace("n", "q")
    s = s.replace("o", "r")
    s = s.replace("p", "s")
    s = s.replace("q", "t")
    s = s.replace("r", "u")
    s = s.replace("s", "v")
    s = s.replace("t", "w")
    s = s.replace("u", "x")
    s = s.replace("v", "y")
    s = s.replace("w", "z")
    s = s.replace("x", "a")
    s = s.replace("y", "b")
    s = s.replace("z", "c")
    return s
