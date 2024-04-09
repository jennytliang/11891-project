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
        if ch.isupper():
            return ch.lower()
        elif ch.islower():
            return ch.upper()
        else:
            return ch
    
    def vowel_replace(ch):
        if ch.lower() in 'aeiou':
            if ord(ch) + 2 < 123:
                return chr(ord(ch) + 2)
            else:
                return chr(ord(ch) - 26)
        else:
            return ch
            
    return ''.join([switch_case(vowel_replace(char)) for char in message])

if __name__ == '__main__':
    import doctest
    doctest.testmod()