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
	Do not include these tokens in the code: # Write your code here .
	"""
    s = s.lower()
    d = {'a':'x', 'b':'y', 'c':'z', 'd':'a', 'e':'b', 'f':'c', 'g':'d', 'h':'e', 'i':'f', 'j':'g', 'k':'h', 'l':'i', 'm':'j', 'n':'k', 'o':'l', 'p':'m', 'q':'n', 'r':'o', 's':'p', 't':'q', 'u':'r', 'v':'s', 'w':'t', 'x':'u', 'y':'v', 'z':'w'}
    r = ''
    for i in s:
        if i in d:
            r += d[i]
        else:
            r += i
    return r

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'lm'
    decrypt('asdfghjkl') returns 'ewhjklnop'
    decrypt('gf') returns 'kj'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: # Write your code here .
	"""
    s = s.lower()
    d = {'x':'a', 'y':'b', 'z':'c', 'a':'d', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'f':'i', 'g':'j', 'h':'k', 'i':'l', 'j':'m', 'k':'n', 'l':'o', 'm':'p', 'n':'q', 'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v', 't':'w', 'u':'x', 'v':'y', 'w':'z'}
    r = ''
    for i in s:
        if i in d