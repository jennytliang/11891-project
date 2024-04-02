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
    

def encode_substitution(s: str):
    """
    returns encoded string by substituting "e","o" for "3","0".
    """
    return s.replace("o", "3").replace("e", "0")


def decode_substitution(s: str):
    """
    takes as input string encoded with encode_substitution fuction. Returns decoded string.
    Do not include these tokens in the code: (
    """
    return s.replace("3", "o").replace("0", "e")    
    
    
def encode_substitution_for_digits(s: str):
    """
    returns encoded string with numbers 3 and 0 instead of e and o. 
    """
    return s.replace("o", "3").replace('O', "3").replace("l", "1").replace('L', "1").replace('e', '0').replace('E', '0')


def decode_substitution_for_digits(s: str):
    """
    takes as input string encoded with encode_substitution_for_digits fuction. Returns decoded string.
    
    Do not include these tokens in the code: (
	"""

    return s.replace("3", "o").replace("0", "e").replace("1", "l")        