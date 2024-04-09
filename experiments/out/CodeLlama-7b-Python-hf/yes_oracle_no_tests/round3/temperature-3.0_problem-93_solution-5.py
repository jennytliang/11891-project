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
	Do not include these tokens in the code: result = '' for
	"""
    # YOUR CODE HERE
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([switch_case(ch) if ch in vowels else ch for ch in message.lower()])

def switch_case(ch):
    """
    Helper function that switches the case of a character
    """
    if ch.islower():
        return ch.upper()
    else:
        return ch.lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

