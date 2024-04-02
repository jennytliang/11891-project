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
    # YOUR CODE HERE
    vowels = 'aeiou'
    result = []
    for c in message:
        if c.lower() in vowels:
            result.append(vowels[(vowels.index(c.lower()) + 2) % 5])
        else:
            result.append(c.upper() if c.isupper() else c.lower())
    return ''.join(result)


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
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    vowels = 'aeiou'
    result = []
    for c in message:
        if c.lower() in vowels:
            result.append(vowels[(vowels.index(c.lower()) - 2) % 5])
        else:
            result.append(c.upper() if c.isupper() else c.lower())
    return ''.join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
