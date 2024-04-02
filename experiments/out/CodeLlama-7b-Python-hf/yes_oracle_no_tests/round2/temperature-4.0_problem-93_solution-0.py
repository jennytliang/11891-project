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
    vowels = "aeiou"
    for i in range(len(message)):
        if message[i] in vowels:
            message = message[:i] + message[i].upper() + message[i+1:].replace(message[i], chr((ord(message[i]) + 2 - 97) % 26 + 97), 1)
        else:
            message = message[:i] + message[i].upper() + message[i+1:]
    return message


def encode_without_replace(message):
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
    vowels = "aeiou"
    for i in range(len(message)):
        if message[i] in vowels:
            message = message[:i] + message[i].upper() + message[i+1:].replace(message[i], chr((ord(message[i]) + 2 - 97) % 26 + 97), 1)
        else:
            message = message[:i] + message[i].upper() + message[i+1:]
    return message


def encode_with_replace(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
