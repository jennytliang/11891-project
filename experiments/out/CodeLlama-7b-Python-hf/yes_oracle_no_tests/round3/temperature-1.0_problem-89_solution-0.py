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
    
	Include these tokens in the code: return " ". join ( map ( lambda ch :
	"""


    d = 'abcdefghijklmnopqrstuvwxy'
    d1 = 'cdefghijklmnopqrstuvwxyab'
    s = s.lower()
    s = s.replace(' ','')
    s = s.replace('a','a')
    s = s.replace('b','b')
    s = s.replace('c','c')
    s = s.replace('d','d')
    s = s.replace('e','e')
    s = s.replace('f','f')
    s = s.replace('g','g')
    s = s.replace('h','h')
    s = s.replace('i','i')
    s = s.replace('j','j')
    s = s.replace('k','k')
    s = s.replace('l','l')
    s = s.replace('m','m')
    s = s.replace('n','n')
    s = s.replace('o','o')
    s = s.replace('p','p')
    s = s.replace('q','q')
    s = s.replace('r','r')
    s = s.replace('s','s')
    s = s.replace('t','t')
    s = s.replace('u','u')
    s = s.replace('v','v')
    s = s.replace('w','w')
    s = s.replace('x','x')
    s = s.replace('y','y')
    s = s.replace('z','z')
    s = s.replace('a','a')
    s = s.replace('b','b')
    s = s.replace('c','c')
    s = s.replace('d','d')
    s = s.replace('e','e')
    s = s.replace('f','f')
    s = s.replace('g','g')
    s = s.replace('h','h')
    s = s.replace('i','i')
    s = s.replace('j','j')
    s = s.replace('k','k')
    s = s.replace('l','l')
    s