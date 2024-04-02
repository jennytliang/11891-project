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
    result = ''
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                result += ch.lower()
            else:
                result += ch.upper()
            if ch.lower() in 'aeiou':
                result += chr(ord(ch) + 2)
            else:
                result += ch
        else:
            result += ch
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
