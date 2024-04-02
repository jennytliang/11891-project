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
	Do not include these tokens in the code: result = ''
	"""
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    for ch in message:
        if ch in alphabet:
            if ch in vowels:
                result += alphabet[(alphabet.index(ch) + 2) % len(alphabet)]
            else:
                result += alphabet[alphabet.index(ch) ^ 1]
        else:
            result += ch
    return result


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
	Do not include these tokens in the code: result = ''
	"""
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    for ch in message:
        if ch in alphabet:
            if ch in vowels:
                result += alphabet[(alphabet.index(ch) - 2) % len(alphabet)]
            else:
                result += alphabet[alphabet.index(ch) ^ 1]
        else:
            result += ch
    return result
