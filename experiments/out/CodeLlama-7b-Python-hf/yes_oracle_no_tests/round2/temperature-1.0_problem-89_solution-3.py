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
    
    s = list(s)
    for i, letter in enumerate(s):
        i = d(int(i)*2)
        s[i] = encriptletter(letter) 
    
    
    
    return "".join(s)    
    


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and returns
    a string decrypted with the alphabet being rotated as in the encrypt function. 
    
    For example: 
    decrypt('lm') returns 'hi'
    decrypt('ewhjklnop') returns 'asdfghjkl'
    decrypt('kj') returns 'gf'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: decrypt
	"""
    
    s = list(s)
    for i, letter in enumerate(s):
        i = d(int(i)) - 2
        s[i] = encriptletter(letter) 
    
    
    
    return "".join(s)    
            
        


    
    
def encriptletter(letter):
    """Helper function that takes in a letter (string)
    and returns the string equivalent to the letter being
    rotated right.
    
    For example:
    encriptletter('a') returns 'c'
    encriptletter('b') returns 'd'
    
    Do not include these tokens in the code:
    encrypt
    d
    """
    # write
    newletter = chr(97+(ord(letter)%2)+(ord(letter)-97)//3)
    return newletter
    
    



def d(n):
    """Helper function for rotating the alphabet. 
    Takes in a number between 0 and 3 as an argument.
    
    Do not include these tokens in the code: d
    """
    return(n%4)   