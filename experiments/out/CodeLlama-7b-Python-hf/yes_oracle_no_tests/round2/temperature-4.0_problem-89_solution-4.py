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
    
	Include these tokens in the code: abc def gh ij kl mn op q
	Do not include these tokens in the code: i j
	"""

    
    s = list(s)
    for i in range(len(s)):
        if s[i] == 'a':
            s[i] = 'e'
        elif s[i] == 'b':
            s[i] = 'f'
        elif s[i] == 'c':
            s[i] = 'g'
        elif s[i] == 'd':
            s[i] = 'h'
        elif s[i] == 'e':
            s[i] = 'i'
        elif s[i] == 'f':
            s[i] = 'j'
        elif s[i] == 'g':
            s[i] = 'k'
        elif s[i] == 'h':
            s[i] = 'l'
        elif s[i] == 'i':
            s[i] = 'm'
        elif s[i] == 'j':
            s[i] = 'n'
        elif s[i] == 'k':
            s[i] = 'o'
        elif s[i] == 'l':
            s[i] = 'p'
        elif s[i] == 'm':
            s[i] = 'q'
        elif s[i] == 'n':
            s[i] = 'r'
        elif s[i] == 'o':
            s[i] = 's'
        elif s[i] == 'p':
            s[i] = 't'
        elif s[i] == 'q':
            s[i] = 'u'
        elif s[i] == 'r':
            s[i] = 'v'
        elif s[i] == 's':
            s[i] = 'w'
        elif s[i] == 't':
            s[i] = 'x'
        elif s[i] == 'u':
            s[i] = 'y'
        elif s[i] == 'v':
            s[i] = 'z'
        elif s[i] == 'w':
            s[i] = '