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
	Do not include these tokens in the code: v ow els = [' a ',
	"""
    # YOUR CODE HERE
    #vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #message = list(message)
    #for i in range(len(message)):
    #    if message[i] in vowels:
    #        message[i] = message[i].swapcase()
    #        message[i] = message[i].replace(message[i], alphabet[alphabet.index(message[i])+2])
    #return ''.join(message)
    #return ''.join(list(map(lambda x: x.swapcase() if x in vowels else x.replace(x, alphabet[alphabet.index(x)+2]), message)))
    return ''.join(list(map(lambda x: x.swapcase() if x in 'aeiou' else x.replace(x, alphabet[alphabet.index(x)+2]), message)))


def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'TEST'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
    """
    # YOUR CODE HERE
    #vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #message = list(message)
    #for i in range(len(message)):
    #    if message[i] in vowels:
    #        message[i] = message[i].swapcase()
    #        message[i] = message[i].replace(message[i], alphabet[alphabet.index(message[i])-2])
    #return ''.join