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
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    # YOUR CODE HERE
    message = message.lower()
    encoded_message = ""
    for ch in message:
        if ch == 'a':
            encoded_message += 'C'
        elif ch == 'e':
            encoded_message += 'G'
        elif ch == 'i':
            encoded_message += 'H'
        elif ch == 'o':
            encoded_message += 'J'
        elif ch == 'u':
            encoded_message += 'M'
        elif ch == 'y':
            encoded_message += 'V'
        elif ch in 'aeiouy':
            encoded_message += chr(ord(ch) + 2)
        else:
            encoded_message += ch
    return encoded_message
    

def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('tgst')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    # YOUR CODE HERE
    message = message.lower()
    decoded_message = ""
    for ch in message:
        if ch == 'c':
            decoded_message += 'A'
        elif ch == 'g':
            decoded_message += 'E'
        elif ch == 'h':
            decoded_message += 'I'
        elif ch == 'j':
            decoded_message += 'O'
        elif ch == 'm':
            decoded_message += 'U'
        elif ch == 'v':
            decoded_message += 'Y'
        elif ch in 'cghiouy':
            decoded_message += chr(ord(ch) - 2)
       