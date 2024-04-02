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
    new_s = s.encode('ascii', 'ignore')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    translation_dict = {'abc'=> 'cde', 'def'=>'efg', 'ghi'=>'jkl', 'mno'=>'pqr', 'pqr'=>'stu', 'stu'=>'vwx'}
    new_s = s.translate(s.maketrans(alphabet, "cdefghijklmnopqrstuvwx"))
    return new_s
    print(new_s)