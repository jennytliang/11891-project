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
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    message = message.lower()
    return ''.join(switch(letter) if letter in 'aeiou' else letter for letter in message)


def switch(letter):
    """
    Write a function that takes a letter, and returns the letter that 
    appears 2 places ahead of that letter in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> switch('a')
    'c'
    >>> switch('z')
    'b'
    """
    # YOUR CODE HERE
    return chr(ord(letter) + 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
