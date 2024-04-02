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
    
	Include these tokens in the code: '
	Do not include these tokens in the code: "
	"""

   # return "".join(chr((ord(i) + 0)%255 if i.isalpha() else i) for i in s)
<<<<<<< HEAD
    return "".join(chr((ord(i) + 10)%255 if i.isalpha() else i) for i in s)


print(encrypt('qwertyuiopasdfghjklzxcvbnm'))
=======
	return "".join(chr((ord(i) + 10)%256 if i.isalpha() else i) for i in s)


print(encrypt('qwertyuiopasdfghjklzxcvbnm'))
>>>>>>> 66468767b5d223865a9d983bd1d9ecc530c04119
