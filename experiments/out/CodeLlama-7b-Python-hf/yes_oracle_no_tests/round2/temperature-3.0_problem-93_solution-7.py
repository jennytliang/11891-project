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
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: result = '' message =
	"""
    result = ''
    message = message.lower()
    for letter in message:
        if letter in "aeiou":
            result += chr(ord(letter) + 2)
        elif letter in "AEIOU":
            result += chr(ord(letter) + 2).upper()
        else:
            result += letter
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
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: result = '' message =
	"""
    result = ''
    message = message.lower()
    for letter in message:
        if letter in "aeiou":
            result += chr(ord(letter) - 2)
        elif letter in "AEIOU":
            result += chr(ord(letter) - 2).upper()
        else:
            result += letter
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
