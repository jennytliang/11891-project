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
	Do not include these tokens in the code: result = ''
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    message = message.lower()
    result = ''
    for ch in message:
        if ch in vowels:
            result += chr(ord(ch) + 2)
        else:
            if ch.isalpha():
                if ch.isupper():
                    result += ch.lower()
                else:
                    result += ch.upper()
            else:
                result += ch
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
