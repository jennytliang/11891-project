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
        if ch.isalpha():
            if ch.isupper():
                return ch.lower()
            else:
                return ch.upper()
        else:
            return ch

    def encode(msg):
        new_msg = ""
        for ch in msg:
            if ch in "aeiou":
                new_msg += chr((ord(ch) + 2) % 26 + ord('a'))
            else:
                new_msg += switch_case(ch)
        return new_msg

    return encode(message)


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('test')
    'TEst'
    >>> decode('TGST')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""

    def switch_case(ch):
        if ch.isalpha():
            if ch.isupper():
                return ch.lower()
            else:
                return ch.upper()
        else:
            return ch

    def decode(msg):
        new_msg = ""
        for ch in msg:
            if ch in "aeiou":
                new_msg += chr((ord(ch) - 2) % 26 + ord('a'))
            else:
                new_msg += switch_case(ch)
        return new_msg

    return decode(message)
