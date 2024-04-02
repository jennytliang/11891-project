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
    
	Do not include these tokens in the code: s = str ( s )
	"""
    LETTERS = '! " # $ % & \' () * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z'
    CLS = len(LETTERS )
    result = ''
    for c in s:
        if not c in LETTERS:
            result += c
            continue
        idx=LETTERS.find(c)
        idx=idx-2*2
        if idx<0:
            idx+=CLS
        result += LETTERS[idx]
    return result

print(encrypt('hi'))
