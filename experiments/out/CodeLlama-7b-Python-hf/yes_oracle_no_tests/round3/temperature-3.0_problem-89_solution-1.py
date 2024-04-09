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
    
	Include these tokens in the code: abc
	"""

    
    s = s.lower()
    result = ""
    for i in s:
        if i == 'a':
            result = result + 'c'
        elif i == 'b':
            result = result + 'd'
        elif i == 'c':
            result = result + 'e'
        elif i == 'd':
            result = result + 'f'
        elif i == 'e':
            result = result + 'g'
        elif i == 'f':
            result = result + 'h'
        elif i == 'g':
            result = result + 'i'
        elif i == 'h':
            result = result + 'j'
        elif i == 'i':
            result = result + 'k'
        elif i == 'j':
            result = result + 'l'
        elif i == 'k':
            result = result + 'm'
        elif i == 'l':
            result = result + 'n'
        elif i == 'm':
            result = result + 'o'
        elif i == 'n':
            result = result + 'p'
        elif i == 'o':
            result = result + 'q'
        elif i == 'p':
            result = result + 'r'
        elif i == 'q':
            result = result + 's'
        elif i == 'r':
            result = result + 't'
        elif i == 's':
            result = result + 'u'
        elif i == 't':
            result = result + 'v'
        elif i == 'u':
            result = result + 'w'
        elif i == 'v':
            result = result + 'x'
        elif i == 'w':
            result = result + 'y'
        elif i == 'x':
            result = result + 'z'
        elif i == 'y':
            result = result + 'a'
        elif i == 'z':
            result = result + 'b'
        elif i == ' ':
            result = result + ' '
        else:
            result = result + i
    return result



print(enc