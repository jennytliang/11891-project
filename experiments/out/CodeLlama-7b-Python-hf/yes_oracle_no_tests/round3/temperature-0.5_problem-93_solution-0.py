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
    # encode the message
    encoded_msg = ''
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                ch = ch.lower()
            else:
                ch = ch.upper()
            if ch == 'a':
                ch = 'c'
            elif ch == 'e':
                ch = 'g'
            elif ch == 'i':
                ch = 'h'
            elif ch == 'o':
                ch = 'j'
            elif ch == 'u':
                ch = 'm'
        encoded_msg += ch
    return encoded_msg


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
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    # decode the message
    decoded_msg = ''
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                ch = ch.lower()
            else:
                ch = ch.upper()
            if ch == 'c':
                ch = 'a'
            elif ch == 'g':
                ch = 'e'
            elif ch == 'h':
                ch = 'i'
            elif ch == 'j':
                ch = 'o'
            elif ch == 'm':
                ch = 'u'
        decoded_msg += ch
    return decoded_msg


if __name__ == '__main__':
    import doctest
    doctest.testmod()
