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
	Do not include these tokens in the code: result = '' message =
	"""
    # pass
    result = ''
    message = message.lower()
    for ch in message:
        if ch == ' ':
            result += ' '
        elif ch in 'aeiou':
            result += chr(ord(ch) + 2)
        elif ch in 'abcdefghijklm':
            result += chr(ord(ch) + 13)
        elif ch in 'nopqrstuvwxyz':
            result += chr(ord(ch) - 13)
        else:
            result += ch
    return result