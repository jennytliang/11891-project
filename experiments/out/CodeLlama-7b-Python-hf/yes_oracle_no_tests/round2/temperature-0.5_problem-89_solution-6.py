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
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: # print
	"""


    
    d = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    s = s.replace(' ','')
    s = s.replace('\n','')
    s = s.replace('\t','')
    s = s.replace('\r','')
    s = s.replace(' ','')
    s = s.replace('1','')
    s = s.replace('2','')
    s = s.replace('3','')
    s = s.replace('4','')
    s = s.replace('5','')
    s = s.replace('6','')
    s = s.replace('7','')
    s = s.replace('8','')
    s = s.replace('9','')
    s = s.replace('0','')
    s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace('!','')
    s = s.replace('?','')
    s = s.replace('"','')
    s = s.replace('\'','')
    s = s.replace(':','')
    s = s.replace(';','')
    s = s.replace('-','')
    s = s.replace('_','')
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.replace('&','')
    s = s.replace('%','')
    s = s.replace('=','')
    s = s.replace('+','')
    s = s.replace('[','')
    s = s.replace(']','')
    s = s.replace('{','')
    s = s.replace('}','')
    s = s.replace('*','')
    s = s.replace('/','')
    s = s.replace('|','')
    s = s.replace('<','')
    s = s.replace('>','')
    s = s.replace('0','')
    s = s.replace('1','')
    s = s.replace('2','')
    s = s