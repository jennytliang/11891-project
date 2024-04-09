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
	Do not include these tokens in the code: # code goes here new
	"""
    # code goes here
    # new
    vowels = 'aeiou'
    def switch(c):
        if c in vowels:
            return chr((ord(c) - ord('a') + 2) % 5 + ord('a'))
        if c.isupper():
            return c.lower()
        return c.upper()
    return ''.join(map(switch, message))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
