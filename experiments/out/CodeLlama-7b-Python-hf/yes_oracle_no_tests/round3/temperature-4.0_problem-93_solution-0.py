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
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    message = message.lower()
    for i in message:
        if i in 'aeiou':
            message = message.replace(i, message[message.index(i)+2])
    for i in message:
        if i.isupper():
            message = message.replace(i, i.lower())
        if i.islower():
            message = message.replace(i, i.upper())
    return message


if __name__ == '__main__':
    import doctest
    doctest.testmod()