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
	Do not include these tokens in the code: v ow els = [' a ',
	"""
    message = message.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, char in enumerate(message):
        if char in vowels:
            message = message.replace(char, message[i+2])

    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                message = message.replace(char, message[i].upper())
            else:
                message = message.replace(char, message[i].lower())

    return message


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'TEST'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """
    message = message.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, char in enumerate(message):
        if char in vowels:
            message = message.replace(char, message[i+2])

    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                message = message.replace(char, message[i].upper())
            else:
                message = message.replace(char, message[i].lower())

    return message


if __name__ == "__main__":
    import doctest
    doctest.testmod()
