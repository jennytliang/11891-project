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
    
	Include these tokens in the code: d = '
	Do not include these tokens in the code: return s . translate ( str .
	"""
    print(s)
    ct = ''
    code = {97: 'q', 98: 'w', 99: 'e', 100: 'r', 101: 't', 102: 'y', 103: 'u', 104: 'i', 105: 'o', 106: 'p',  
    107: 'a', 108: 's', 109: 'd', 110: 'f', 111: 'g', 112: 'h', 113: 'j', 114: 'k', 115: 'l', 219: ' ', 116: 'z', 
    117: 'x', 118: 'c', 119: 'v', 120: 'b', 121: 'n', 122: 'm' }
    for e in s:
      if e in code:
        ct += code[e]
      
    print(ct)
    return ct
    
    
encrypt('hi')
encrypt('asdfghjkl')
encrypt('gf')
encrypt('et')