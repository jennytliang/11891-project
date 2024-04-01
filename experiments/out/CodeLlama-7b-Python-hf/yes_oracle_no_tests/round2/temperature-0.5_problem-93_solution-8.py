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
	Do not include these tokens in the code: # encode the message
	"""
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha.upper()
    alpha_encoded = alpha + alpha_upper
    alpha_decoded = alpha_upper + alpha
    vowels = 'aeiou'
    message = message.lower()
    encoded = ''
    for letter in message:
        if letter in alpha:
            if letter in vowels:
                encoded += alpha_encoded[alpha.index(letter) + 2]
            else:
                encoded += alpha_encoded[alpha.index(letter)]
        else:
            encoded += letter
    return encoded


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
    
	Include these tokens in the code: def switch
	Do not include these tokens in the code: # encode the message
	"""
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha.upper()
    alpha_encoded = alpha + alpha_upper
    alpha_decoded = alpha_upper + alpha
    vowels = 'aeiou'
    message = message.lower()
    decoded = ''
    for letter in message:
        if letter in alpha:
            if letter in vowels:
                decoded += alpha_decoded[alpha_encoded.index(letter) - 2]
            else:
                decoded += alpha_decoded[alpha_encoded.index(letter)]
        else:
            decoded += letter
    return decoded


if __name__ == '__main__':
    import doctest
    doctest.testmod()
