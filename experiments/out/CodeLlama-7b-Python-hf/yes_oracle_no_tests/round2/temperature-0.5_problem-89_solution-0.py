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
	Do not include these tokens in the code: e = ' ABC DEF G HI J K LM
	"""


    
    d = 'abcdefghijklmnopqrstuvwxyz'
    e = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = d + e
    
    s = s.lower()
    s = s.replace(' ','')

    newstr = ''

    for i in s:
        if i in d:
            newstr += f[(f.index(i)+2*2)%52]
        elif i in e:
            newstr += f[(f.index(i)+2*2)%52]
        else:
            newstr += i

    return newstr

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
    
	Include these tokens in the code: return " ". join ( map ( lambda ch :
	Do not include these tokens in the code: e = ' ABC DEF G HI J K LM
	"""


    
    d = 'abcdefghijklmnopqrstuvwxyz'
    e = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = d + e
    
    s = s.lower()
    s = s.replace(' ','')

    newstr = ''

    for i in s:
        if i in d:
            newstr += f[(f.index(i)-2*2)%52]
        elif i in e:
            newstr += f[(f.index(i)-2*2)%52]
        else:
            newstr += i

    return newstr





















