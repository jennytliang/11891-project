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
    message = message.lower()
    for i in range(0, len(message)):
        if message[i] in 'aeiou':
            message = message[:i] + chr(ord(message[i]) + 2) + message[i + 1:]
        else:
            message = message[:i] + chr(ord('A') + ord(message[i]) - ord('a')) + message[i + 1:]
    return message


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('test')
    'TGST'
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    message = message.lower()
    for i in range(0, len(message)):
        if message[i] in 'aeiou':
            message = message[:i] + chr(ord(message[i]) - 2) + message[i + 1:]
        else:
            message = message[:i] + chr(ord('a') + ord(message[i]) - ord('A')) + message[i + 1:]
    return message


if __name__ == "__main__":
    import doctest
    doctest.testmod()
