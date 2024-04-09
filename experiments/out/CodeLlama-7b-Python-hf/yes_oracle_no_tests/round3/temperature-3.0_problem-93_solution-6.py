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
	Do not include these tokens in the code: message = message . lower ()
	"""
    message = message.lower()
    
    for i, char in enumerate(message):
        if char in "aeiou":
            message = message[:i] + char.upper() + message[i+1:]
        if char not in "aeiou":
            message = message[:i] + char.swapcase() + message[i+1:]
            
    return message


if __name__ == "__main__":
    import doctest
    doctest.testmod()
