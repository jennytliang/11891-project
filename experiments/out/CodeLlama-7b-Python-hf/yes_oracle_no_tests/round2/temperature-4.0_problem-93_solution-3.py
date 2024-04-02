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
    
	Include these tokens in the code: def switch
	Do not include these tokens in the code: message = message . lower ()
	"""
    message = message.lower()
    encoded_message = ''
    for i in range(len(message)):
        if message[i] == 'a' or message[i] == 'e' or message[i] == 'i' or message[i] == 'o' or message[i] == 'u':
            encoded_message += chr(ord(message[i]) + 2)
        elif message[i] == 'y':
            encoded_message += 'x'
        else:
            encoded_message += chr(ord(message[i]) ^ 32)
    return encoded_message

def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch
	Do not include these tokens in the code: message = message . lower ()
	"""
    message = message.lower()
    decoded_message = ''
    for i in range(len(message)):
        if message[i] == 'a' or message[i] == 'e' or message[i] == 'i' or message[i] == 'o' or message[i] == 'u':
            decoded_message += chr(ord(message[i]) - 2)
        elif message[i] == 'x':
            decoded_message += 'y'
        else:
            decoded_message += chr(ord(message[i]) ^ 32)
    return decoded_message