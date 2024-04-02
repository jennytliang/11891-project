def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: v ow els = ' ae i
	"""
    return "".join(
        [char if char in "aei" else chr(ord(char) + 2).upper() if char.isupper() else chr(ord(char) + 2).lower() for char in message]
    )


def decode(message):
    """
    Write a function that takes a message string and decode, returning the original message. 
    Assume only letters. 

    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'

    """
    return encode(encode(message)[::-1])[::-1]