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
    """
    s = replace(s) # call function
    s_encrypt= s
    for i in range(3) :
        s = shift(s) #call function
    	s_encrypt += s 
    if i % 2 = 0 :   # check if even 
         return s_encrypted[:len(s)/2])+ s_encrypt[(len(s)+1)/2 + 1  ]
    else :  return s_encrypto[ :len(s)//2 ] , s_encrypt[(1)*2 : len(s) )
  
def decrypt(encrypt):
     """Decrypt the message by applying the function encrypt with
	the argument string and returning a string that is a decryption of s"""

     for i  range(2): # reverse first two encryptions 
         encrypt = shift(encrypt )
     