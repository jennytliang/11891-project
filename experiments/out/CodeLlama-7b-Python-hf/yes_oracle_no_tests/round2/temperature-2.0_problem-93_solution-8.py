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
	Do not include these tokens in the code: # pass encoded
	"""
    
    # your code goes here
    def switch(c):
        if c == 'a':
            return 'S'
        elif c == 'e':
            return 'T'
        elif c == 'i':
            return 'A'
        elif c == 'o':
            return 'O'
        elif c == 'u':
            return 'N'
        else:
            return c
    
    def encode_char(c):
        if c in 'aeiou':
            return switch(c)
        else:
            return c
    
    return ''.join(map(encode_char, message))

if __name__ == "__main__":
    import doctest
    doctest.testmod()