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
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_caps = alpha.upper()
    vowels = "aeiou"
    message = message.lower()
    message_encoded = ""
    for letter in message:
        if letter in alpha:
            if letter in vowels:
                message_encoded += alpha[(alpha.index(letter) + 2) % 26]
            else:
                message_encoded += alpha[(alpha.index(letter) + 1) % 26]
        elif letter in alpha_caps:
            if letter in vowels:
                message_encoded += alpha_caps[(alpha_caps.index(letter) + 2) % 26]
            else:
                message_encoded += alpha_caps[(alpha_caps.index(letter) + 1) % 26]
        else:
            message_encoded += letter
    return message_encoded


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('test')
    'RGZH'
    >>> decode('This is a message')
    'TGKS KS C MGSSCGG'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    # YOUR CODE HERE
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_caps = alpha.upper()
    vowels = "aeiou"
    message = message.lower()
    message_decoded = ""
    for letter in message:
        if letter in alpha:
            if letter in vowels:
                message_decoded += alpha[(alpha.index(letter) - 2) % 26