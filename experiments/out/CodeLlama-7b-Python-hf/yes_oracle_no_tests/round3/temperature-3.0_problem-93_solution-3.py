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
	Do not include these tokens in the code: result = '' for
	"""
    # YOUR CODE HERE
    vowels = 'aeiou'
    result = ''
    for ch in message:
        if ch.isalpha():
            if ch.islower():
                ch = ch.upper()
            if ch.lower() in vowels:
                ch = chr(ord(ch.lower()) + 2)
            if ch.isupper():
                ch = ch.lower()
        result += ch
    return result


def encode_mod(message):
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
	Do not include these tokens in the code: result = '' for
	"""
    # YOUR CODE HERE
    vowels = 'aeiou'
    result = ''
    for ch in message:
        if ch.isalpha():
            if ch.islower():
                ch = ch.upper()
            if ch.lower() in vowels:
                ch = chr(ord(ch.lower()) + 2)
            if ch.isupper():
                ch = ch.lower()
        result += ch
    return result


def encode_mod2(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message