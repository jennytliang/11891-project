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
    vowels = ['a','e','i','o','u']
    message = message.lower()
    encoded_message = ''
    for ch in message:
        if ch in vowels:
            encoded_message += chr(ord(ch)+2)
        elif ch.isalpha():
            if ch.isupper():
                encoded_message += ch.lower()
            else:
                encoded_message += ch.upper()
        else:
            encoded_message += ch
    return encoded_message

if __name__ == '__main__':
    import doctest
    doctest.testmod()
