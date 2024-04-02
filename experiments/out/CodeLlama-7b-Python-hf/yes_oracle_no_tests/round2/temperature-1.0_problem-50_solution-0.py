def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_substitute(s: str):
    """
	returns encoded string in which any charater appearing
    in the string 'subs' (any string) is substituted with the 
    next letter in the alphabet. Capital letters are also encoded (but you don't have to worry about 
	capitalizing the substrings for me).
	For example: s = 'I AM A NINJAAAAAGUY'
                 subs = 'NINJA'
                 encode_substitute(s) should return
				 'L J AK KDGWKWGU'.
	"""
    return "".join([ch for ch in s])

def decode_substitute(s:str):
    """
	takes as input string encoded with encode_substitute. Returns decoded string.
	The input string can consist of any character in the alphabet,
	spaces, letters, and numbers.
	The substitution can be for only some of the letters.
	For example, 
	'I AM A NA INJAAAAAGUY' returns 'J N', NOT 'J A N'.
	"""
    return "".join([ch for ch in s])


def encode_multiply(s:str):
    """
	returns encoded string in which every character in the string 'mult'
    (any string) is replaced by that many copies of the character. Be sure to
    encode spaces and numbers as well. 
	For example, s = 'I AM A NA INJAAAAAGUY'
                 mult = 'NINJA'
    encode_multiply(s) should return 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'.
    """
    return "".join([ch for ch in s])

def decode_multiply(s: str):
    """
	takes as input string encoded with encode_multiply function. Returns decoded string.
    """
    return "".join([ch for ch in s])

def encode_shift