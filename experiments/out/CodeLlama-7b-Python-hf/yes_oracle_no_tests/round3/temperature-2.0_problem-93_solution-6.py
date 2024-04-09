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
    
	Do not include these tokens in the code: message = message . lower ()
	"""
    vowels = 'aeiou'
    message = message.lower()
    encoded = ''
    for char in message:
        if char in vowels:
            encoded += chr(ord(char) + 2)
        elif char.isalpha():
            encoded += char.swapcase()
        else:
            encoded += char
    return encoded


def encode_2(message):
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
    
	Do not include these tokens in the code: message = message . lower ()
	"""
    vowels = 'aeiou'
    message = message.lower()
    encoded = ''
    for char in message:
        if char in vowels:
            encoded += chr(ord(char) + 2)
        elif char.isalpha():
            encoded += char.swapcase()
        else:
            encoded += char
    return encoded


def encode_3(message):
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
    
	Do not include these tokens in the code: message = message . lower ()
	"""
    vowels = 'aeiou'
    message = message.lower()
    encoded = ''
    for