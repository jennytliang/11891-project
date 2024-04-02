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
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    vowels = 'aeiou'
    new_message = ''
    for ch in message:
        if ch.islower():
            new_message += ch.upper()
        elif ch.isupper():
            new_message += ch.lower()
        elif ch in vowels:
            new_message += chr(ord(ch) + 2)
        else:
            new_message += ch
    return new_message


def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('test')
    'TGST'
    >>> decode('This is a message')
    'tHKS KS C MGSSCGG'
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    vowels = 'aeiou'
    new_message = ''
    for ch in message:
        if ch.islower():
            new_message += ch.upper()
        elif ch.isupper():
            new_message += ch.lower()
        elif ch in vowels:
            new_message += chr(ord(ch) - 2)
        else:
            new_message += ch
    return new_message


if __name__ == '__main__':
    import doctest
    doctest.testmod()
