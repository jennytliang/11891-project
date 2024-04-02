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
    message = message.lower()
    for i in range(len(message)):
        if message[i] in 'aeiou':
            result += chr(ord(message[i]) + 2)
        elif message[i].isalpha():
            result += message[i].swapcase()
        else:
            result += message[i]
    return result


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('tgst')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: result = ''
	"""
    result = ''
    message = message.lower()
    for i in range(len(message)):
        if message[i] in 'aeiou':
            result += chr(ord(message[i]) - 2)
        elif message[i].isalpha():
            result += message[i].swapcase()
        else:
            result += message[i]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
