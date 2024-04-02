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
	Do not include these tokens in the code: # My first code , works but
	"""
    message += 'x' * 2
    def switch_case(ch):
        if ch in 'aeiou' :
            return chr((ord(ch) - ord('a') + 2) % 26 + ord('a'))
        else :
            return ch.lower() if ch.isupper() else ch.upper()
    return ''.join([switch_case(ch) for ch in message])