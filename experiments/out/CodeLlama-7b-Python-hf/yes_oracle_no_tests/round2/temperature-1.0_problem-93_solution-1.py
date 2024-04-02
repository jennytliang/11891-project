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
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    def switch_case(ch):
        if ch.islower():
            return ch.upper()
        else:
            return ch.lower()

    def vowels(ch):
        vowels = "aeiou"
        if ch in vowels:
            return vowels[(vowels.index(ch)+2) % len(vowels)]
        else:
            return ch

    def encode(message):
        return "".join([switch_case(vowels(ch)) for ch in message])


    return encode(message)




















