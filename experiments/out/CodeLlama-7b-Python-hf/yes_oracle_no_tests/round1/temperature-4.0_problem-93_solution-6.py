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
	Do not include these tokens in the code: d = {} d ['
	"""
    
    def switch(char):
        if char.islower():
            return char.upper()
        elif char.isupper():
            return char.lower()
        else:
            return char
    
    d = {
        'a': 'c',
        'e': 'g',
        'i': 'h',
        'o': 'j',
        'u': 'l',
        'c': 'a',
        'g': 'e',
        'h': 'i',
        'j': 'o',
        'l': 'u'
    }

    result = []
    for char in message:
        if char.lower() in d:
            result.append(switch(char))
            result.append(d[char.lower()])
        else:
            result.append(switch(char))
    return ''.join(result)


def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
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
	Do not include these tokens in the code: d = {} d ['
	"""
    
    def switch(char):
        if char.islower():
            return char.upper()
        elif char.isupper():
            return char.lower()
        else:
            return char
    
    d = {
        'a': 'c',
        'e': 'g',
        'i': 'h',
        'o': 'j',
        'u': 'l',
        'c': 'a',
        'g': 'e',
        'h': 'i',
        'j': 'o',
        'l': 'u'