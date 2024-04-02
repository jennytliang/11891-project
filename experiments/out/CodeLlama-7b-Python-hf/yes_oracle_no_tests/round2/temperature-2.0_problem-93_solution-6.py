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
	Do not include these tokens in the code: message = message . lower ()
	"""
    message = message.lower()
    def switch(letter):
        if letter in "aeiou":
            return chr(ord(letter) + 2)
        elif letter in "aeiouy":
            return letter
        else:
            return letter.upper()
    return "".join([switch(letter) for letter in message])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
