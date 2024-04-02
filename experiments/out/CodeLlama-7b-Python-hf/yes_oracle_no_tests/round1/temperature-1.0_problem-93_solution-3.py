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
    def switch_case(ch):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            return chr(ord(ch) + 2)
        elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            return chr(ord(ch) + 2)
        else:
            return ch

    result = ''
    for ch in message:
        result += switch_case(ch)
    return result


def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places behind that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('tgst')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    def switch_case(ch):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            return chr(ord(ch) - 2)
        elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            return chr(ord(ch) - 2)
        else:
            return ch

    result = ''
    for ch in message:
        result += switch_case(ch)
    return result
