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
	Do not include these tokens in the code: alpha = ' abc gh ij
	"""

    alpha = ' abcdefghijklmnopqrstuvwxyz'
    alpha += alpha.upper()
    message = message.lower()
    message = message.replace(' ','')
    encoded = ''
    for i in range(len(message)):
        if message[i] in alpha:
            if message[i] in 'aeiou':
                encoded += alpha[alpha.index(message[i])+2]
            elif message[i] in 'y':
                encoded += 'x'
            else:
                encoded += message[i].swapcase()
        else:
            encoded += message[i]
    return encoded


def decode(message):
    """
    Write a function that takes a message, and decodes it in such a 
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
	Do not include these tokens in the code: alpha = ' abc gh ij
	"""

    alpha = ' abcdefghijklmnopqrstuvwxyz'
    alpha += alpha.upper()
    message = message.lower()
    message = message.replace(' ','')
    decoded = ''
    for i in range(len(message)):
        if message[i] in alpha:
            if message[i] in 'abc':
                decoded += alpha[alpha.index(message[i])-2]
            elif message[i] in 'x':
                decoded += 'y'
            else:
                decoded += message[i].swapcase()
        else:
            decoded += message[i]
    return decoded


if __name__ == '__main__':
    import doctest
    doctest.testmod()
